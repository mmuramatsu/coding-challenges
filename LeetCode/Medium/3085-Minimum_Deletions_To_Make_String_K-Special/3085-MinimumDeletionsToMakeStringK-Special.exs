defmodule Solution do
  @doc """
  Calculates the minimum number of characters to delete to make the string k-special.
  """
  def minimum_deletions(word, k) do
    # String.graphemes() return a list with character of the string, like
    # "hi" -> ['h','i'].

    # |> pipe operator. It takes the result of the expression on its left and
    # passes it as the first argument to the function on its right.

    # Enum.reduce iterating over an enumerable and accumulate the result. the
    # first argument is a empty map "%{}" and the second argument is a "lambda"
    # function. This function is called for each element in the list.
    # &(&1 + 1): This is another anonymous function (a shorthand syntax). It's a
    # function that takes one argument (&1) and returns &1 + 1. This function is
    # called only if char is already present in acc. The current value associated
    # with char in acc is passed as &1, and we increment it.
    freq =
      String.graphemes(word)
      |> Enum.reduce(%{}, fn char, acc ->
        Map.update(acc, char, 1, &(&1 + 1))
      end)

    ans = String.length(word)

    freq_values = Map.values(freq)

    # Outer Enum.reduce
    # Similar to "for key, value in freq.items():"
    Enum.reduce(freq_values, ans, fn x, current_min_ans ->
      deletions_for_x =
        # Inner Enum.reduce
        Enum.reduce(freq_values, 0, fn y, deletions ->
          if x > y do
            deletions + y
          else
            if y > x + k do
              deletions + (y - (x + k))
            else
              deletions
            end
          end
          end)

      min(current_min_ans, deletions_for_x)
    end # Closes the outer `fn` block
    ) # Closes the outer `Enum.reduce` call
  end
end