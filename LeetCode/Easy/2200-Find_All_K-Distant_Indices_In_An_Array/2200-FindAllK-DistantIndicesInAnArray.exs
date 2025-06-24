defmodule Solution do
  @spec find_k_distant_indices(nums :: [integer], key :: integer, k :: integer) :: [integer]
  # Close to the sequential version. faster
  def find_k_distant_indices(nums, key, k) do
    find_key(Enum.drop(nums, 0), 0, 0, length(nums), key, k, [])
  end

  defp find_key([], _i, _right, _n, _key, _k, ans), do: ans

  defp find_key([curr | rest], i, right, n, key, k, ans) do
    if curr == key do
      left = Enum.max([right, i - k])
      right = Enum.min([n - 1, i + k]) + 1
      interval = add_to_ans(left, right, [])

      find_key(rest, i+1, right, n, key, k, ans ++ interval)
    else
      find_key(rest, i+1, right, n, key, k, ans)
    end
  end

  defp add_to_ans(idx, right, ans) do
    if idx < right do
      curr = ans ++ [idx]
      add_to_ans(idx + 1, right, curr)
    else
      ans
    end
  end

  # Using MapSet + sort. Slower
  def find_k_distant_indices(nums, key, k) do
    n = length(nums)

    key_idx = Enum.with_index(nums)
      |> Enum.filter(fn {val, _idx} -> val == key end)
      |> Enum.map(fn {_val, idx} -> idx end)

    affected_indices_set = MapSet.new()

    ans = Enum.reduce(key_idx, affected_indices_set, fn i, acc_set ->
      left = Kernel.max(0, i - k)
      right = Kernel.min(n - 1, i + k)

      Enum.reduce(left..right, acc_set, fn j, current_set ->
        MapSet.put(current_set, j)
      end)
    end)

    ans |> MapSet.to_list() |> Enum.sort()
  end
end
