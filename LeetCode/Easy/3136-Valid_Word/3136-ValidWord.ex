defmodule Solution do
  @spec is_valid(word :: String.t) :: boolean
  def is_valid(word) do
    Regex.match?(~r/^(?=.*[aeiou])(?=.*[^aeiou0-9])[a-z0-9]{3,}$/i, word)
  end
end
