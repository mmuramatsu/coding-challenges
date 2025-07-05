defmodule Solution do
  @spec kth_character(k :: integer, operations :: [integer]) :: char
  def kth_character(k, operations) do
    exp = get_curr_len(k, 1, 0)

    curr_len = 2**exp
    t = exp - 1
    new_k = k - 1

    final_char = calculate_final_char(curr_len, t, new_k, operations, 97)

    if final_char > 122 do
      final_char - 26
    else
      final_char
    end
  end

  defp get_curr_len(k, len, t) do
    if len <= k do
      get_curr_len(k, len * 2, t+1)
    else
      t
    end
  end

  defp calculate_final_char(curr_len, _t, _new_k, _op, final_char) when curr_len == 1 do final_char end

  defp calculate_final_char(curr_len, t, k, op, final_char) do
    new_curr_len = curr_len / 2

    if k >= new_curr_len do
      new_k = k - new_curr_len

      if Enum.at(op, t) == 1 do
        calculate_final_char(new_curr_len, t-1, new_k, op, final_char+1)
      else
        calculate_final_char(new_curr_len, t-1, new_k, op, final_char)
      end
    else
      calculate_final_char(new_curr_len, t-1, k, op, final_char)
    end
  end
end
