defmodule Solution do
  @spec max_distance(s :: String.t, k :: integer) :: integer
  def max_distance(s, k) do
    initial_state = %{
        north: 0,
        south: 0,
        east: 0,
        west: 0,
        ans: 0
    }

    final_state = String.graphemes(s) |> Enum.with_index() |> Enum.reduce(initial_state, fn
        {"N", i}, %{north: north, south: south, east: east, west: west, ans: current_ans} ->
            new_north = north + 1

            conflicts = min(new_north, south) + min(east, west)
            max_dist = calculate_max_dist(i + 1, conflicts, k)

            new_ans = max(current_ans, max_dist)

            %{north: new_north, south: south, east: east, west: west, ans: new_ans}

        {"S", i}, %{north: north, south: south, east: east, west: west, ans: current_ans} ->
            new_south = south + 1

            conflicts = min(north, new_south) + min(east, west)
            max_dist = calculate_max_dist(i + 1, conflicts, k)

            new_ans = max(current_ans, max_dist)

            %{north: north, south: new_south, east: east, west: west, ans: new_ans}

        {"E", i}, %{north: north, south: south, east: east, west: west, ans: current_ans} ->
            new_east = east + 1

            conflicts = min(north, south) + min(new_east, west)
            max_dist = calculate_max_dist(i + 1, conflicts, k)

            new_ans = max(current_ans, max_dist)

            %{north: north, south: south, east: new_east, west: west, ans: new_ans}

        {"W", i}, %{north: north, south: south, east: east, west: west, ans: current_ans} ->
            new_west = west + 1

            conflicts = min(north, south) + min(east, new_west)
            max_dist = calculate_max_dist(i + 1, conflicts, k)

            new_ans = max(current_ans, max_dist)

            %{north: north, south: south, east: east, west: new_west, ans: new_ans}

    end
    )

    final_state.ans

  end

  defp calculate_max_dist(max_dist, conflicts, k) do
        if k < conflicts do
            max_dist - (conflicts * 2) + (k * 2)
        else
            max_dist
        end
    end
end
