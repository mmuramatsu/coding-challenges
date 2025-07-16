# Problem: 3201 - Find the Maximum Length of Valid Subsequence I (MEDIUM)

## Problem statement:

Given an integer array `nums`, or task is to find the length of the longest subsequence that satify:

`(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.`

## Intuition:

First, let's think about this expression. When we do `(sub[0] + sub[1]) % 2`, we're verifing if this sum is odd or even. We know the following rule of summing number. Let $E$ be a even number and $O$ an odd number, we have:

$$E + E = E \\
E + O = O \\
O + E = O \\
O + O = E$$

With that, if we have that `sub[0]` and `sub[1]` are even so we have `sub[0] + sub[1]` even. For `nums[i]` to be part of this subsequence, it need to be even too, so we have `sub[1] + nums[i]` even. Similarly, for `sub[0]` and `sub[1]` odd, we need `nums[i]` to be odd too to form a subsequence.

If we have `sub[0]` even and `sub[1]` odd, we have `sub[0] + sub[0]` odd. For `nums[i]` to part of the subequence we need `sub[1] + nums[i]` to be odd too. The unique way to do this is if `nums[i]` is even. Similarly, for `sub[0]` odd and `sub[1]` even, the next value need to be odd.

Thus, we have four possibilities of longest subsequence.
- a subsequence full of even values;
- a subsequence full of odd values;
- a subsequence starting with even value and alternating odd/even;
- a subsequence starting with odd value and alternating even/odd.

Following this line, the first two subsequences is basically count how much even values and odd values we have, respectively. The other two, we need to count how many alternations we have, starting with even and odd. Remembering that we're interested in subsequences, so the numbers don't need to be in adjacents.

A simple loop checking the parity of the each value in `nums` and updating the counter variables can solve this problem. At the end we simply get the maximum of the four counts.

### Complexity:
- Time complexity: $O(N)$

- Space complexity: $O(1)$