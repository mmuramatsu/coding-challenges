defmodule Solution do
  @spec possible_string_count(word :: String.t) :: integer
  def possible_string_count(word) do
    word_list = String.graphemes(word)
    do_count(Enum.at(word_list, 0), Enum.drop(word_list, 1), 1)
  end

  defp do_count(_prev, [], count), do: count

  defp do_count(prev, [curr | rest], count) do
    if prev == curr do
      do_count(curr, rest, count + 1)
    else
      do_count(curr, rest, count)
    end
  end
end
