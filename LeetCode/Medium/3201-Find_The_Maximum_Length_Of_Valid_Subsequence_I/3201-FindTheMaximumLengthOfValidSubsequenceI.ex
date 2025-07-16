defmodule Solution do
  @spec maximum_length(nums :: [integer]) :: integer
  def maximum_length(nums) do
    initial_state = %{
      odd: 0,
      even: 0,
      alt_even: 0,
      alt_odd: 0,
      next_even: true,
      next_odd: true
    }

    final_state = Enum.reduce(nums, initial_state, fn num, acc ->
      is_odd = rem(num, 2) != 0

      new_acc = Map.merge(acc, %{
        odd: if(is_odd, do: acc.odd + 1, else: acc.odd),
        even: if(not is_odd, do: acc.even + 1, else: acc.even)
      })

      new_acc =
        if is_odd do # Current number is ODD
          if acc.next_odd do
            Map.put(new_acc, :alt_odd, acc.alt_odd + 1)
            |> Map.put(:next_odd, false)
          else
            new_acc
          end
        else # Current number is EVEN
          if not acc.next_odd do
            Map.put(new_acc, :alt_odd, acc.alt_odd + 1)
            |> Map.put(:next_odd, true)
          else
            new_acc
          end
        end

      new_acc =
        if not is_odd do # Current number is EVEN
          if acc.next_even do
            Map.put(new_acc, :alt_even, acc.alt_even + 1)
            |> Map.put(:next_even, false)
          else
            new_acc
          end
        else # Current number is ODD
          if not acc.next_even do
            Map.put(new_acc, :alt_even, acc.alt_even + 1)
            |> Map.put(:next_even, true)
          else
            new_acc
          end
        end

      new_acc
    end)

    Enum.max([
      final_state.odd,
      final_state.even,
      final_state.alt_odd,
      final_state.alt_even
    ])
  end
end
