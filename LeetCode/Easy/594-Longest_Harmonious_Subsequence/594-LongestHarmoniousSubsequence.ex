defmodule Solution do
  @spec find_lhs(nums :: [integer]) :: integer
  def find_lhs(nums) do
    freq = nums
      |> Enum.reduce(%{}, fn num, acc ->
      Map.update(acc, num, 1, fn count -> count + 1 end)
    end)

    ans = 0

    Enum.reduce(Map.to_list(freq), ans, fn {k, v}, current_ans ->
      if Map.has_key?(freq, k + 1) do
        max(current_ans, v + Map.fetch!(freq, k + 1))
      else
        current_ans
      end
    end)
  end
end
