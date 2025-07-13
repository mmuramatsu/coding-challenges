# Problem: 2410. Maximum Matching of Players With Trainers (MEDIUM)

## Problem statement:

Given an integer array `players`, where `player[i]` represent the ability of the `i`-th player and an integer array `trainers`, where `trainer[j]` represent the training capacity of the `j`-th trainer, we need to match the maximum number of players and trainers. A match can be done if `players[i] <= trainers[j]`.

## Intuition:

To solve this problem we need a way to easily find the optimal trainer that fit a player. For example, if we have the following input, `players = [2,9]` and `trainers = [10, 4]`. In this case, both trainers can train `players[0]`, but the optimal choice is `trainers[1]` so we can match the `players[1]` with `trainers[0]` next.

So, the idea is that we need to find, for each player, a trainer with minimum training capacity that match the current player. An easily way to do this is to sort both arrays, so if the `j`-th trainer can't train the `i`-th player, then the `j`-th can't train the rest of the players neither.

Using a two pointers approach we can find the optimal match for a player. For each player `i`, we need to find a trainer `j`, where `player[i] <= trainer[j]`. If the current `j` is not enough, then we try the next `j + 1`, until we find one that works. If we find, we increment the `count` and `j`, and repeat to the next player.

### Complexity:

Let $N$ and $M$ be the length of `players` and `trainers` arrays, respectively.

- Time complexity: $O(N \ log \ N + M \ log \ M)$
    - Sorting: $O(N \ log \ N + M \ log \ M)$
        - `players`: $O(N \ log \ N)$;
        - `trainers`: $O(M \ log \ M)$;
    - Main loop: $O(N + M)$;

- Space complexity: $O(1)$