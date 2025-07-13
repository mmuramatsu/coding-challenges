defmodule Solution do
  @spec match_players_and_trainers(players :: [integer], trainers :: [integer]) :: integer
  def match_players_and_trainers(players, trainers) do
    sorted_players = Enum.sort(players)
    sorted_trainers = Enum.sort(trainers)

    match_players(sorted_players, sorted_trainers, 0)
  end

  defp match_players([], _trainers, count), do: count

  defp match_players(_players, [], count), do: count

  defp match_players([curr_player | rest_p], [curr_trainer | rest_t], count) do
    if curr_player <= curr_trainer do
      match_players(rest_p, rest_t, count + 1)
    else
      match_players([curr_player | rest_p], rest_t, count)
    end
  end
end
