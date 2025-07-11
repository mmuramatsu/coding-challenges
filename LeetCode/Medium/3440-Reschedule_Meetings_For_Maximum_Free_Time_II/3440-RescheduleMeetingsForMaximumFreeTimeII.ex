defmodule Solution do
  @spec max_free_time(event_time :: integer, start_time :: [integer], end_time :: [integer]) :: integer
  def max_free_time(event_time, start_time, end_time) do
    extended_startTime = start_time ++ [event_time]
    extended_endTime = [0] ++ end_time

    gaps = Enum.zip(extended_startTime, extended_endTime) |> Enum.map(fn {s, e} -> s - e end)

    gaps_tuple = List.to_tuple(gaps)

    sorted_gaps = Enum.sort(gaps) |> Enum.reverse() |> Enum.take(3)

    meetings = Enum.zip(start_time, end_time) |> Enum.map(fn {s, e} -> e - s end)

    # Use Enum.reduce to iterate through meetings and maintain state
    Enum.reduce(meetings, {1, 0}, fn duration, {j, max_free_time} ->
      # Find a gap that can fit this meeting
      founded = find_fitting_gap(sorted_gaps, duration, elem(gaps_tuple, j - 1), elem(gaps_tuple, j))

      curr_free_time =
        if founded do
          elem(gaps_tuple, j - 1) + duration + elem(gaps_tuple, j)
        else
          elem(gaps_tuple, j - 1) + elem(gaps_tuple, j)
        end

      new_max_free_time = max(max_free_time, curr_free_time)

      {j + 1, new_max_free_time}
    end)
    |> elem(1) # Extract the final max_free_time
  end

  defp find_fitting_gap(sorted_gaps, duration, gap_left, gap_right) do
    # Since Elixir lists are singly linked, reversing and then iterating is often more efficient
    # for "last element first" type of searches.
    Enum.reduce_while(sorted_gaps, {false, true, true}, fn current_gap, {found, equal_left, equal_right} ->
      if current_gap >= duration do
        cond do
          equal_left and current_gap == gap_left ->
            {:cont, {found, false, equal_right}}
          equal_right and current_gap == gap_right ->
            {:cont, {found, equal_left, false}}
          true -> # Found a gap that's not one of the special ones, or special ones are already "used"
            {:halt, {true, true, true}} # The last two true values are just placeholders as we halt
        end
      else
        {:cont, {found, equal_left, equal_right}}
      end
    end)
    |> case do
      {true, _, _} -> true
      {false, _, _} -> false
    end
  end
end
