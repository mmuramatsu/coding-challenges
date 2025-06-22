defmodule Solution do
  @spec divide_array(nums :: [integer], k :: integer) :: [[integer]]
  def divide_array(nums, k) do
    sorted_nums = Enum.sort(nums)

    do_partition(sorted_nums, k, [])
  end

  # Base case
  defp do_partition([], _k, ans), do: Enum.reverse(ans)

  # Valid case. We preppend the list in the `ans`
  defp do_partition([first, second, third | rest], k, ans) when third - first <= k do
    do_partition(rest, k, [[first, second, third] | ans])
  end

  # Invalid case, return []
  defp do_partition(_invalid, _k, ans), do: []
end