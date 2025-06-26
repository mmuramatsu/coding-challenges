defmodule Solution do
  @spec longest_subsequence(s :: String.t, k :: integer) :: integer
  def longest_subsequence(s, k) do
    s_reverse = String.graphemes(s) |> Enum.reverse()

    {_final_num, final_length, _final_power} = Enum.reduce(s_reverse, {0,0,1}, fn char, {num, length, power} ->
        case char do
            "1" ->
                if num + power <= k do
                    new_num = num + power
                    new_length = length + 1
                    new_power = power * 2
                    {new_num, new_length, new_power}
                else
                    {num, length, power}
                end
            "0" ->
                new_length = length + 1
                new_power = power * 2
                {num, new_length, new_power}
        end
    end)

    final_length
  end
end
