defmodule Solution do
  @spec find_lucky(arr :: [integer]) :: integer
  def find_lucky(arr) do
    freq = arr
      |> Enum.reduce(%{}, fn num, acc ->
      Map.update(acc, num, 1, fn count -> count + 1 end)
    end)

    ans = -1

    Enum.reduce(Map.to_list(freq), ans, fn {k, v}, current_ans ->
      if k == v and k > current_ans do
        k
      else
        current_ans
      end
    end)
  end
end
