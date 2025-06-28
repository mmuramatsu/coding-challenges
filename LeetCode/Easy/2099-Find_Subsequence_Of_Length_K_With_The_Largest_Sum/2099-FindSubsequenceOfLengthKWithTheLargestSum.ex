defmodule Solution do
  @spec max_subsequence(nums :: [integer], k :: integer) :: [integer]
  def max_subsequence(nums, k) do
    idx_nums = Enum.with_index(nums)

    greatest = idx_nums
      |> Enum.sort(fn {a, _idx_a}, {b, _idx_b} ->
        a > b
      end)
      |> Enum.take(k)

    idx_greatest = greatest
      |> Enum.sort(fn {_a, idx_a}, {_b, idx_b} ->
        idx_a < idx_b
      end)

    ans = Enum.map(idx_greatest, fn {num, _idx} -> num end)

    ans
  end
end
