# Problem: 3333 - Find the Original Typed String II (HARD)

## Problem statement

Given a string `word`, which can have repeated characters due to miss typing, and an integer `k`, our task is to find the total number of possible original strings that Alice might have intended to type, if she was trying to type a string of size at least `k`.

## Intuition

Instead of looking for the strings with length greater than or equal to `k`, it's easy to calculate all possible strings and then substract from the possible strings with length less than `k`.

To find the total possible strings we can split the string into groups of repeated sequences and get the sizes, for example, the string `"aabbccdd"` and `k = 7`, the groups will be `groups = [2, 2, 2, 2]`. The `total` is the product of all groups sizes. So the total number of possible string is `total = 2 x 2 x 2 x 2 = 16`.

One optimization can be done here. The minimum length that we can obtain is given by the length of `groups` array. The problem of the string is that some characters may get pressed for too long, but if it appears in the string, then it must appear at least once. In our example, the minimum lenght is `len(groups) = 4`, which lead us to the string `"abcd"`. So, if `len(gropus) >= k`, then, all possible strings will have a length greater or equal to `k`, so we can return the `total` in this case.

To calculate the number of possible strings of length less than `k`, we're going to use a DP with Prefix Sum approach. Let's define the arrays `dp` and `ps` as our dynamic programming table and prefix sum array, respectively. Both, `dp` and `ps` are of length `k`, so `dp[i]` represents the number of strings of length `i` and `ps` is the prefix sum of the `dp` array.

Starting from `length = 0`, only the empty string can satisfy this condition. So, we initialize the `ps` array full of $1$. The `dp` array will be initialized full of $0$.

We're going to iterate through each group sizes and for each groups size we're going the iterate through all possible `length` from `1` to `k - 1` calculatating the number of possible string of each length `length`. In our example, the first groups has size $2$, which is `"aa"`. With this we can form two strings, `"a"` or  `"aa"`. So, `dp[1] = 1` and  `dp[2] = 1`. We can't form a string of length $3$ or greater with this group, so `dp[3] = dp[4] = ... = 0`.

After that we update the `ps` array with the values of `dp` (reset all position of `ps` to $0$ and recalculate the prefix sum using this current `dp` table.)

For reference, currently we have `ps = [0,1,2,2,2,2,2]`.

Heading to the next group, with size $2$ too. We need to reset our `dp` array and recalculate for all the lengths again considering the previous groups processed. The previous possible strings is `"a"` and `"aa"`, so we can't form string with `length = 1` by appending `"b"` or `"bb"`, so `dp[1] = 0`. For `length = 2` we have `"ab"`, so `dp[2] = 1`. For `length = 3` we have `"abb"`, `"aab"`, so `dp[3] = 2`. For `length = 4` we only have `"aabb"`, so `dp[4] = 1`. For the next lengths `dp` will be $0$. So we have `dp = [0,0,1,2,1,0,0]`.

We can properly define our DP recurence as `dp[i] = ps[length - 1] - impossible_length`, where `impossible_length` is defined as `ps[length - size - 1]` if `length - size - 1 >= 0`, otherwise $0$. The idea here is that we can only form a valid string of length `length` if we append strings of length `length - 1`, `length - 2`, ..., `length - size` to it. For example, with the string `"a"`, we can't form a valid string of length $4$ using a group of size $2$, because neither `"ab"` or `"abb"` has length $4$. So, we can only form a valid string of `length = 4`, with string of `length = 3` or `length = 2`, or we can say `ps[length - 1] - ps[length - size - 1]` (with the second term we're removing the invalid length strings.).

So, let's redo that last step. For `length = 1`, we have `dp[1] = ps[0] = 0`. For `length = 2`, we have `dp[2] = ps[1] = 1`. For `length = 3`, we have `dp[3] = ps[2] - ps[0] = 2`. For `length = 4`, we have `dp[4] = ps[3] - ps[1] = 1`. For `length = 5`, we have `dp[5] = ps[4] - ps[2] = 0`. Finally, for `length = 6`, we have `dp[6] = ps[5] - ps[3] = 0`. So we have `dp = [0,0,1,2,1,0,0]`, which are correct.

So, by the end of this we have the total number of invalid string at `ps[k - 1]`, so our return will be `total - ps[k - 1]`, and that's the number of possible string of length `k` or greater.



