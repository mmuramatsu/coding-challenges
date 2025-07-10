defmodule Solution do
  @spec max_free_time(event_time :: integer, k :: integer, start_time :: [integer], end_time :: [integer]) :: integer
  def max_free_time(event_time, k, start_time, end_time) do
    extended_startTime = start_time ++ [event_time]
    extended_endTime = [0] ++ end_time

    gaps = Enum.zip(extended_startTime, extended_endTime) |> Enum.map(fn {s, e} -> s - e end)

    gaps_tuple = List.to_tuple(gaps)
    n_gaps = tuple_size(gaps_tuple)

    max_free_time = 0
    curr_free_time = 0..k-1 |> Enum.map(&elem(gaps_tuple, &1)) |> Enum.sum()

    {_final_sum, final_max_free_time, _final_left} =
      Enum.reduce(k..n_gaps-1, {curr_free_time, max_free_time, 0}, fn right, {acc_sum, acc_max, left} ->
        new_sum = acc_sum + elem(gaps_tuple, right)
        new_max = max(acc_max, new_sum)
        removing_left = new_sum - elem(gaps_tuple, left)
        new_left = left + 1

        {removing_left, new_max, new_left}
      end)
    final_max_free_time
  end
end
