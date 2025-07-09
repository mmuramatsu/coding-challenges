# Problem: 1751 - Maximum Number of Events That Can Be Attended II (HARD)

## Problem statement

Given an array `events` where `events[i] = [startDayi, endDayi, valuei]` and an integer `k`, our task is to select `k` non-overlapping events that maximize the value.

## Intuition:

This problem reminds me of "0/1 Knapsack" problem, where we need to maximize the value of the items in a bag that don't pass the weight limit. In this problem we can say that each event has a "weight" of 1 and we want to maximize the value of the selected events.

Based on that, we going to use DP to solve this problem. Each event `i` has two possible states, `skip` or `attned`. If we skip the `i`-th event, the total value and the number of events that we can attend still the same. If we attend to the `i`-th event, we add the value of the `i`-th event, reduce the number of events that we can attend and try the next possible event that don't overlap the current one.

We can define our `dp` as:
- `dp[event_idx][k] = max(skip, attend)`

One optimization that we can do is to precompute the next possible event for all events in `events`. If we attend to an event, we must attend the full duration of it, so we next possible event is the first event has `startDay` greater than the `endDay` of the current event. The idea is, first we sort `events` array based on the `startDay`, then for each event we apply binary search (`bisect_right`) to find the next possible `startDay`, with that we avoid recalculating during the solving part.

## Solution 1 - Top-down DP + Binary search:

In the Top-down approach, we going to define a matrix `memo`, `n` by `k + 1`, where we going to store the maximum value obtained by choosing `k` events between `n` events. All the positions of `memo` will be initialize as `-1`.

We also going to define a function `solve(event_idx, k)` to find the answer recursively. The base case is when `k == 0` or  `event_idx >= n`. The fisrt case, we can't attend to more events so we return 0. The second case, there's no more events to try, so we also return 0 If `mem[event_idx][k] != -1`, it means that we already calculate this, so we simply return `mem[event_idx][k]`.

Then we calculate the value if we skip or attend `event_idx`, which will be:
- `skip = solve(event_idx + 1, k)`;
- `attend = solve(next_event, k - 1) + events[event_idx][2]`.

The result for `memo[event_idx][k]` is `max(skip, attend)`. After that, we return `memo[event_idx][k]`.

This function will calculate the right answer for the problem and return to the main functoin, so we simply return `solve(0, k)`.

### Complexity:
- Time complexity: $O (N \ log \ N + N \cdot K)$
    - Sorting: $O(N \ log \  N)$;
    - Precomputation: $O(N \ log \ N)$;
    - DP calls: $O(N \cdot K)$.

- Space complexity: $O(N \cdot K)$
    - `memo` table: $O(N \cdot K)$;
    - `start_day` array $O(N)$;
    - `next_event` array $O(N)$.


## Solution 2 - Botton-up DP + Binary search:

The Botton-up approach, we need to defina a `dp` table which has size of `n + 1` by `k + 1`, where we going to store the maximum value obtained by choosing `k` events between `n` events. All the positions of `dp` will be initialize as `0`.

Differently from the Top-down approach the order is important. The `event_idx` needs to iterate from `n-1` down to `0`. (Because `dp[i]` depends on `dp[i+1]` or `dp[next_event]` where `next_event >= i+1`). The `k_remaining` needs to iterate from `1` up to `K`. (Because `dp[...][j]` depends on `dp[...][j-1]`).

For the Botton-up approach, we need to manually initialize the base case on our table. We need to do `dp[i][0] = 0` for all `i`, meaning that we have 0 events remaining, then the value is `0`. We also need to do `dp[N][j] = 0` for all `j`, meaning that if there are no events left to consider from index `N` onwards, the value is `0`. But we're already doing this by initialize the `dp` with `0`.

As we said before, we're going to have two nested loops. The first one will iterate through the events backwards (`n-1` to `0`), we can call `event_idx` as before. The second loop will iterate through `k` (`1` to `k`) let's call `k_reminder`.

Inside this we're going to do the same as the Top-down version, calculate `skip` and `attend` and calculate `dp[event_idx][k]`, which is:
- `skip = dp[event_idx + 1][k]`;
- `attend = dp[next_event][k - 1] + events[event_idx][2]`;
- `dp[event_idx][k] = max(skip, attend)`.

After the loops ends, the result will be in `dp[0][k]`.

### Complexity:

- Time complexity: $O (N \ log \ N + N \cdot K)$
    - Sorting: $O(N \ log \  N)$;
    - Precomputation: $O(N \ log \ N)$;
    - Table filling: $O(N \cdot K)$.

- Space complexity: $O(N \cdot K)$
    - `dp` table: $O(N \cdot K)$;
    - `start_day` array $O(N)$;
    - `next_event` array $O(N)$.
