defmodule Solution do
  @spec kth_character(k :: integer) :: char
  def kth_character(k) do
    shifts = k - 1
      |> Integer.to_string(2)
      |> String.graphemes()
      |> Enum.count(fn bit -> bit == "1" end)

    97 + shifts
  end
end
