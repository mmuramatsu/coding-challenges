# Problem: 455 - Assign Cookies (EASY)

## Problem statement:

Given an integer array `g`, where `g[i]` represent the greedy of the `i`-th kid and an integer array `s`, where `s[j]` represent the size of the `j`-th cookie, we need to match the maximum number of kid and cookies. A match can be done if `g[i] <= s[j]`.

## Intuition:

To solve this problem we need a way to easily find the optimal cookie that satisfy a kid. For example, if we have the following input, `g = [2,9]` and `g = [10, 4]`. In this case, both cookies can satisfy `g[0]`, but the optimal choice is `s[1]` so we can match the `g[1]` with `s[0]` next.

So, the idea is that we need to find, for each kid, a cookie with minimum size that match the current kid. An easily way to do this is to sort both arrays, so if the `j`-th cookie can't satisfy the `i`-th kid, then the `j`-th can't satisfy the rest of the kids neither.

Using a two pointers approach we can find the optimal match for a kid. For each kid `i`, we need to find a cookie `j`, where `g[i] <= s[j]`. If the current `j` is not enough, then we try the next `j + 1`, until we find one that works. If we find, we increment the `count` and `j`, and repeat to the next kid.

### Complexity:

Let $N$ and $M$ be the length of `g` and `s` arrays, respectively.

- Time complexity: $O(N \ log \ N + M \ log \ M)$
    - Sorting: $O(N \ log \ N + M \ log \ M)$
        - `g`: $O(N \ log \ N)$;
        - `s`: $O(M \ log \ M)$;
    - Main loop: $O(N + M)$;

- Space complexity: $O(1)$