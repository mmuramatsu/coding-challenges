# Problem: 594 - Longest Harmonious Subsequence (EASY)

## Problem statement

Given an integer array `nums`, our task is to find the length of the longest harmonious subsequence. An array is considered harmonious if the difference between the maximum and the minimum of the array is exactly $1$.

## Intuition

As the difference between the maximum and the minimum needs to be $1$, the array need to be formed by two unique elements, `x` and `x + 1`. Since we are working with integers, that's the only way we can find a difference of $1$. So, the length of an harmonious subsequence is the sum of the number of repetitions of `x` and `x + 1`.

An efficient way to solve this problem is to count the frequency of each element of `nums` using a Hash Map, then, for each key `k` we verify if `k + 1` is in our Hash Map `freq`. If it is, then we update our answer `ans = max(ans, freq[k] + freq[k + 1])`. At the end of this loop we have the length of the longer harmonious subsequence.