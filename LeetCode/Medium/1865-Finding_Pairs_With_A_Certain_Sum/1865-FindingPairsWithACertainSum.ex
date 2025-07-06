defmodule FindSumPairs do
  # --- Elixir's "Class" and "Object" Simulation ---
  # In Elixir, we don't have classes. Instead, we use modules to group functions
  # and structs to define the "shape" of our data (our "object's state").
  # Data is immutable, so functions take state and return *new* state.

  # 1. Define the struct: This acts as the blueprint for our "object's" internal state.
  defstruct nums2: [], freq1: %{}, freq2: %{}, keys: []

  # 2. Define a type alias for our struct: Improves readability and enables Dialyzer static analysis.
  @type t() :: %__MODULE__{
          nums2: [integer()],
          freq1: %{integer() => integer()}, # Map: number -> frequency
          freq2: %{integer() => integer()},
          keys: [integer()] # Sorted list of unique keys from nums1
        }

  # --- State Management for LeetCode's OOP-centric Test Harness ---
  # This is the "hacky" part for competitive programming platforms.
  # LeetCode expects a shared, mutable "instance" state. In Elixir, true mutable
  # shared state is managed by processes. An Agent is a simple process for this.

  # 3. Name the Agent: This atom will be the "handle" to our "global" state-holding process.
  @find_sum_pairs_agent :find_sum_pairs_state

  # @doc """
  # Constructor: Initializes the FindSumPairs "object".
  # Corresponds to `var FindSumPairs = function(nums1, nums2) { ... }` in JS.
  # On LeetCode, this function is called once per test case to set up the instance.
  # """
  @spec init_(nums1 :: [integer], nums2 :: [integer]) :: pid()
  def init_(nums1, nums2) do
    # Build initial frequency maps.
    freq1 = build_frequency_map(nums1)
    freq2 = build_frequency_map(nums2)

    keys = freq1 # IMPORTANT: Get keys from the *map* (freq1), not the original list (nums1)
      |> Map.keys()
      |> Enum.sort()

    # Create the initial state struct. This is the "object" we want the Agent to hold.
    state_to_init = %__MODULE__{
      nums2: nums2,
      freq1: freq1,
      freq2: freq2,
      keys: keys
    }

    # 4. Agent Lifecycle Management: Handling LeetCode's test runner behavior.
    # LeetCode often runs test cases sequentially without fully resetting the Erlang VM.
    # This means a named Agent from a previous test case might still be running.
    # We must ensure a clean start for each test case.
    case Agent.start_link(fn -> state_to_init end, name: @find_sum_pairs_agent) do
      {:ok, pid} ->
        # Agent started successfully, return its PID (this is what LeetCode expects as the "object handle").
        pid
      {:error, {:already_started, pid}} ->
        # If the Agent is already running (from a previous test case),
        # we explicitly stop the old one and then start a new one.
        # This guarantees a fresh state for the current test case.
        Agent.stop(pid) # Stop the existing process by its PID.
        # After stopping, try starting again. This time it should succeed.
        {:ok, new_pid} = Agent.start_link(fn -> state_to_init end, name: @find_sum_pairs_agent)
        new_pid
      {:error, reason} ->
        # Catch any other unexpected errors during Agent startup.
        raise "Failed to start agent: #{inspect reason}"
    end
  end

  # Helper function (private, `defp`) to avoid code duplication for frequency map building.
  defp build_frequency_map(list) do
    Enum.reduce(list, %{}, fn num, acc ->
      Map.update(acc, num, 1, fn count -> count + 1 end)
    end)
  end

  # @doc """
  # Adds `val` to `nums2[index]` and updates frequencies.
  # Corresponds to `FindSumPairs.prototype.add = function(index, val) { ... }` in JS.
  # LeetCode expects this to be called without explicitly passing the object state.
  # """
  @spec add(index :: integer, val :: integer) :: :ok # LeetCode often expects "void" return for mutators.
  def add(index, val) do
    # 5. Accessing and Updating State via Agent:
    # `Agent.update` is used when you need to read the current state, transform it,
    # and set a new state. It's atomic (thread-safe).
    Agent.update(@find_sum_pairs_agent, fn state ->
      # All logic inside this anonymous function operates on the 'state' variable,
      # which is the current FindSumPairs struct held by the Agent.
      # Remember: all Elixir data structures are immutable.
      # Updating means creating new versions of them.

      old_val = Enum.at(state.nums2, index) # Get old value from nums2 list (immutable)
      new_val = old_val + val

      # Update freq2: Decrement old_val's frequency.
      # If count becomes 1, delete the key to save memory and keep map clean.
      # This prevents the map from growing indefinitely with zero-count keys.
      updated_freq2 =
        case Map.get(state.freq2, old_val) do
          nil -> state.freq2 # Should not happen if index is valid and nums2 is non-empty
          1 -> Map.delete(state.freq2, old_val) # Best practice: remove key if count is 0
          count -> Map.put(state.freq2, old_val, count - 1)
        end

      # Update freq2: Increment new_val's frequency.
      updated_freq2 = Map.update(updated_freq2, new_val, 1, fn count -> count + 1 end)

      # Update nums2: List.replace_at returns a *new* list with the element replaced.
      updated_nums2 = List.replace_at(state.nums2, index, new_val)

      # Crucially, return the *new, updated* state struct.
      # This new struct becomes the Agent's internal state for future calls.
      %FindSumPairs{state | nums2: updated_nums2, freq2: updated_freq2}
    end)
    :ok # Return :ok as a common "void" equivalent in Elixir.
  end

  # @doc """
  # Counts pairs.
  # Corresponds to `FindSumPairs.prototype.count = function(tot) { ... }` in JS.
  # LeetCode expects this to be called without explicitly passing the object state.
  # """
  @spec count(tot :: integer) :: integer
  def count(tot) do
    # 6. Accessing State via Agent (Read-Only):
    # `Agent.get` is used to read the current state without modifying it.
    # It passes the current state to the anonymous function, and the function's
    # return value is what `Agent.get` (and thus `count`) returns.
    Agent.get(@find_sum_pairs_agent, fn state ->
      # All logic inside this anonymous function operates on the 'state' variable.
      Enum.reduce(state.keys, 0, fn k1, acc ->
        # Optimization: Keys are sorted. If k1 is already too big, no further
        # k1 values will yield a valid k2 (tot - k1 > 0).
        if k1 >= tot do
          acc # Stop processing and return the accumulated count.
        else
          k2 = tot - k1

          # Get frequencies using Map.get. Use 0 as default if key not found.
          freq1_val = Map.get(state.freq1, k1, 0)
          freq2_val = Map.get(state.freq2, k2, 0)

          # Accumulate the product of frequencies.
          acc + (freq1_val * freq2_val)
        end
      end)
    end)
  end
end
