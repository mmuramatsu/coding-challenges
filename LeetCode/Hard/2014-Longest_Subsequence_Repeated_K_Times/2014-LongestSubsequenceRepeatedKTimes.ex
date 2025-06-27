defmodule Solution do
  @spec longest_subsequence_repeated_k(s :: String.t, k :: integer) :: String.t
  def longest_subsequence_repeated_k(s, k) do
    freq = s
      |> String.graphemes()
      |> Enum.reduce(%{}, fn char, acc ->
      Map.update(acc, char, 1, fn count -> count + 1 end)
    end)

    possible_chars = Enum.to_list(freq)
      |> Enum.filter(fn {_, count} -> count >= k end)
      |> Enum.map(fn {char, _} -> char end)
      |> Enum.sort()

    queue = [""]
    ans = ""

    bfs(queue, ans, s, k, possible_chars)
  end

  defp bfs([], ans, _s, _k, _possible_chars) , do: ans

  defp bfs([curr_subseq | rest], ans, s, k, possible_chars) do
    new_ans = curr_subseq

    next =
      for c <- possible_chars do
        candidate = curr_subseq <> c
        if is_subsequence(s, candidate, k) do
          candidate
        else
          nil
        end
      end
      |> Enum.filter(&(&1 != nil))

    new_queue = rest ++ next

    bfs(new_queue, new_ans, s, k, possible_chars)
  end

  defp is_subsequence(s, subseq, k) do
    target = String.duplicate(subseq, k)

    check(String.to_charlist(s), String.to_charlist(target))
  end

  # This is the standard two-pointer/recursive subsequence check for charlists.
  defp check(_s, []) do
    true # All target characters found
  end
  defp check([], _target) do
    false # Target characters remaining but no more source characters
  end
  defp check([s_head | s_tail], [t_head | t_tail]) do
    if s_head == t_head do
      # Match: advance both
      check(s_tail, t_tail)
    else
      # No match: advance only source
      check(s_tail, [t_head | t_tail])
    end
  end
end
