# Problem: 3202 - Find the Maximum Length of Valid Subsequence II (MEDIUM)

## Problem statement:

Given an integer array `nums` and an integer `k`, or task is to find the length of the longest subsequence that satify:

`(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.`

## Intuition:

First of all, let's analyse the expression. Let `sub[0]`, `sub[1]` and `sub[2]` be `a`,`b` and `c`, respectively. We have:

$$a + b \pmod k= b + c \pmod k$$

This statement means that $a + b$ and $b + c$ have the same remainder when divided by $k$. In terms of congruence, this is written as:

$$a + b \equiv b + c \pmod k$$

Subtracting $b$ in both sides:

$$
(a + b) - b \equiv (b + c) - b \pmod k \\
a \equiv c \pmod k
$$

Which directly means that $a \pmod k = c \pmod k$

Based on that, we have two ways to make a subsequence:
- a subsequence full of same reminder values, meaning $a \equiv b \equiv c \pmod k$;
- an alternate subsequence, where $a \equiv c \pmod k$ and the next element of the subsequence being equal to $b \pmod k$.

We also know that the reminder of a number divided by `k` can be any value from `0` to `k-1`. Thus, to calculate the length of this subsequence we're going to use Dynamic Programming. Let `dp` be our DP table, where `dp[i][j]` is the longest valid subsequence ending with `i` with `j` being the previous element under mod `k`. The size of the `dp` table will be `k`x`k`, initialized with zeros.

For each number of `nums` we need to try every single possible value of reminder as the previous element of the subsequence and see what is the longest subsequence that we can form. So, let `curr = nums[i] % k` for each `prev` in the interval `[0, k - 1]` the transition will be `dp[curr][prev] = dp[prev][curr] + 1`.

With this expression we're basically saying what we have founded so far. Let's reuse the $a$, $b$ and $c$ to make it clear but this time, suposse we have the reminder of $a$, $b$ and $c$ divided by `k`. Suppose we already have a longest subsequence formed by $a$ and $b$. In this case, the longest subsequence including $c$ will be `dp[c][b] = dp[b][a] + 1`. Because $a \equiv c \pmod k$, the state `dp[b][a]` is effectively the same as `dp[b][c]` in terms of the modular relationship for extending the sequence.

So the idea to use two nested loops, the first one will iterate through the numbers of `nums` and the second through the possible values of reminder (from `0` to `k-1`). At the end of this, we have the maximum in `dp` table as the answer.

### Complexity:
- Time complexity: $O(N \cdot K)$
    - main loop: $O(N \cdot K)$.

- Space complexity: $O(K^2)$
    - `dp` matrix: $O(K^2)$;
    - other variables: $O(1)$.