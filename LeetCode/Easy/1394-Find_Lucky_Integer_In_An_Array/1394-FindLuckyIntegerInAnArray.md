# Problem: 1394 - Find Lucky Integer in an Array (EASY)

## Problem statement

Given an integer array `arr`, our task is to find the largest **lucky integer**. A **lukcy integer** is an integer that belongs to `arr` that has a frequency equal to its value. If there's no **lucky integer** we return `-1`.

## Intuition

We can use a Hash Map `freq` to get count the frequency of each element in `arr`. Let's define our answer variable as `ans = -1`. For each `(k, v)` in `freq`, if `k == v and k > ans`, we do `ans = k`. At the end of this loop we have the largest **lucky integer** in `arr`, or `-1` if none are founded.

### Complexity:
- Time complexity: $O(N)$
    - To build `freq` `dict` we need to iterate through all elements of `arr`, so $O(N)$;
    - Let $M$ be the number of unique elements in `arr`. To find the **lucky integers** we loop through all $M$ elements, so $O(M)$;
    - The time complexity is then $O(N + M)$, but since the dominant step is to build `freq`, because $M \le N$. Thus, the time complexity is $O(N)$.
- Space complexity: $O(N)$
    - To store `freq` we need an $O(M)$ space complexity. But in the worst case, $M = N$ (all elements are unique), so the space complexity is $O(N)$.