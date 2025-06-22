defmodule Solution do
  @spec divide_string(s :: String.t, k :: integer, fill :: char) :: [String.t]
  def divide_string(s, k, fill) do
    n = String.length(s)

    s =
      if rem(n, k) != 0 do
        s <> String.duplicate(<<fill>>, k - rem(n, k))
      else
        s
      end

    # In Elixir, the last expression evaluated in a function is its return value.
    for i <- 0..(n - 1) // k do
      String.slice(s, i, k)
    end
  end
end