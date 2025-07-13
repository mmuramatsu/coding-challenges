defmodule Solution do
  @spec find_content_children(g :: [integer], s :: [integer]) :: integer
  def find_content_children(g, s) do
    sorted_g = Enum.sort(g)
    sorted_s = Enum.sort(s)

    match_kid(sorted_g, sorted_s, 0)
  end

  defp match_kid([], _size, count), do: count

  defp match_kid(_greedy, [], count), do: count

  defp match_kid([curr_greedy | rest_g], [curr_size | rest_s], count) do
    if curr_greedy <= curr_size do
      match_kid(rest_g, rest_s, count + 1)
    else
      match_kid([curr_greedy | rest_g], rest_s, count)
    end
  end
end
