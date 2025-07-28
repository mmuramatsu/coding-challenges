defmodule Solution do
  @spec make_fancy_string(s :: String.t) :: String.t
  def make_fancy_string(s) do
    s_list = String.to_charlist(s)
    if length(s_list) < 3 do
      s
    end

    {ans, _prev_char, _count} =
      Enum.reduce(tl(s_list), {[hd(s_list)], hd(s_list), 1}, fn char, {acc, prev, count} ->
        if prev == char do
          new_count = count + 1
          if new_count < 3 do
            {[char | acc], char, new_count}
          else
            {acc, char, new_count}
          end
        else
          {[char | acc], char, 1}
        end
      end)
    Enum.reverse(ans) |> List.to_string()
  end
end
