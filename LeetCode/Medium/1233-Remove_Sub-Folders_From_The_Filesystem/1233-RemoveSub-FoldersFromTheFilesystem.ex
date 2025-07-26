defmodule Solution do
  @spec remove_subfolders(folder :: [String.t]) :: [String.t]
  def remove_subfolders(folder) do
    sorted_folder = Enum.sort(folder)

    final_ans = Enum.reduce(Enum.drop(sorted_folder, 1), [Enum.at(sorted_folder, 0)], fn path, acc ->
      prev_folder = "#{hd(acc)}/"

      if not String.starts_with?(path, prev_folder) do
        [path | acc]
      else
        acc
      end
    end)

    final_ans
  end
end
