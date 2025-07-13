# Problem: 1900 - The Earliest and Latest Rounds Where Players Compete (HARD)

## Problem statement:

It's given an integer `n` representing the number of players from 0 to `n - 1`, an integer `firstPlayer` and an integer `secondPlayer`. We need to simulate a tournament in which, in each round, the `i`-th player from the front of the row competes against the `i`-th player from the end of the row (`1` with `n - 1`, then `2` with `n - 2`, etc.), and the winner advances to the next round. When the number of players is odd for the current round, the player in the middle automatically advances to the next round.

The `firstPlayer` and the `secondPlayer` will win all their matches, the others we can decide any of then to win. Our task is to return the **earliest** possible round number and the **latest** possible round number in which these two players will compete against each other, respectively.

## Intuition:

We're going to use a boolean array (or a bit mask) to mark the players that are alive in the tournament, let's call `alive`. If a player is alive, the correspondent position will be `True`, otherwise `False`. We're going to subtract one from `firstPlayer` and `secondPlayer` to make then `0`-indexed.

The idea is to create a recursive function that will simulate the confronts by using two pointers to mark the opponents. Let's `i` and `j` indicate the players of the confront. `i` will start at `0` and `j` at `n - 1`. Our function `solve` will be a series of `if`s. Let, `min_round` and `max_round` be the variable that store the minimum and maximum number of rounds to `firstPlayer` and `secondPlayer` face each other, respectively. Also, let `round` be the variable that store the current round. The idea is:

- if `i >= r`, it means that we have simulate all the confronts in this round, so we call `solve` reseting `i` and `j` and increment `round`;
- else if `alive[i] != True`, means that the `i`-th player was defeated before, so we call the `solve` function with `i + 1`;
- else if `alive[j] != True`, means that the `j`-th player was defeated before, so we call the `solve` function with `j - 1`;
- else if `i == firstPlayer and j == secondPlayer`, we find the confront that we're looking for, so we update the `min_round` and `max_round`;
- else, both player are alive, so:
    - if `i`-th player is not `firstPlayer` and `secondPlayer`, means that this player can lose, so we call the `solve` function letting `j` win this confront;
    - if `j`-th player is not `firstPlayer` and `secondPlayer`, means that this player can lose, so we call the `solve` function letting `i` win this confront.

At the end of this recursion we have our answer in `min_round` and `max_round`.

With only this we can solve the problem but this will lead us to TLE. We need to add Memorization to avoid calculate the same confronts, but using `i`, `j` and `alive` as state will lead us to MLE, so we need to find other way to define the states.

The thing is, this problem is not about the confronts, we can say that this problem is based on geometry. If we split the players in two sets, we can say that we will only have `firstPlayer` versus `secondPlayer` when they are in the same position in each half. Also, if we make a player win in the first half, we basically is making a shift on the seconde half. For example: if `firstPlayer = 1` versus `secondPlayer = 4`, we can say that this is the order:

    1 2 3 4 5

The first half is `1 2` and the second half `4 5`, and `3` will pass. In this case `1` will win, resulting in:

    1 2 3 4

note that the first half still as `1 2`, and the second half `3 4`. We basically shift `4` one position in the half.

So the states will be defined by 3 variables `l_count`, `m_count` and `r_count`, representing the number of elements on the left of `firstPlayer`, in between `firstPlayer` and `secondPlayer` and after `secondPlayer`, respectively.

With this, we need to change only the `else` of the `solve` function.

- else if, `memo[l_count][m_cound][r_count] != True`, means that we have a unseem state so we need to calculate:
    - if `i`-th player is not `firstPlayer` and `secondPlayer`, means that this player can lose, so we call the `solve` function letting `j` win this confront. We need to update `l_count`, `m_count` and `r_count` as we make `i` lose;
    - if `j`-th player is not `firstPlayer` and `secondPlayer`, means that this player can lose, so we call the `solve` function letting `i` win this confront. We need to update `l_count`, `m_count` and `r_count` as we make `j` lose;

### Complexity:
- Time complexity: $O(N^4)$

- Space complexity: $O(N^3)$
    - `memo` array: $O(N^3)$;
    - `alive`: $O(N)$.