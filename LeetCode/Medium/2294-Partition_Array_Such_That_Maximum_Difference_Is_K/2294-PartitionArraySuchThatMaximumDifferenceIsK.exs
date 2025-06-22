defmodule Solution do
  @spec partition_array(nums :: [integer], k :: integer) :: integer
  def partition_array(nums, k) do
    sorted_nums = Enum.sort(nums)

    do_partition(Enum.drop(sorted_nums, 1), k, 1, Enum.at(sorted_nums, 0) + k)
  end

  # Base case: When the list is empty, return the accumulated count.
  defp do_partition([], _k, ans, _max_value), do: ans

  # Recursive case:
  # Check if the head of the list (curr_num) exceeds the current partition's limit.
  defp do_partition([curr_num | rest], k, ans, max_value) do
    if curr_num > max_value do
      do_partition(rest, k, ans + 1, curr_num + k)
    else
      do_partition(rest, k, ans, max_value)
    end
  end
end