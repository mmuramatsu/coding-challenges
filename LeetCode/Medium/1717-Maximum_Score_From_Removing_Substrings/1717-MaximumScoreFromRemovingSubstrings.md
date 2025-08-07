# Problem: 1717 - Maximum Score From Removing Substrings (MEDIUM)

## Problem statement:

Given a string `s` and two integers `x` and `y`, our task is to remove occurences of `"ab"` and `"ba"` from `s`. Each remotion will be rewarded with a score. If we remove `"ab"` from `s` we score `x`. If we remove `"ba"` from `s` we score `y`. The goal is to find the maximum score after applying this operations.

## Intuition:

To solve this problem, we gonna use a two pass greedy approach. The idea is to remove all occurences of `"ab"` or `"ba"` in the first pass, and the other in the scond pass.

There's is two major points to solve this problem. The first is to choose which substring we will remove first, `"ab"` or `"ba"`. Following a greedy approach, we should remove the one with the highest score first. By removing the higher-scoring substring first, we prevents the characters from becoming part of a lower-scoring substring. This will ensures that we exhaust all possibilities for the higher-scoring substring first, which is the most profitable move at each step.

the second major point of this problem is how to remove the substring from `s` correctly. For example, `s = "aabb"`, we can remove two occurences of `"ab"`. The first one are in `s[1]` and `s[2]`, and the second one is the remaing string after the first operation that form `"ab"`. One way to make the remotion is by use a Stack. We start with an empty Stack and for each character of `s`, we check if the current character with the top of the stack form a substring that we are looking for. If this is true, we pop the top element from it, making a remotion. If not, we simple push the current character to the Stack.

At the end of this process we've removed all occurences of some substring. We just need to repeat this for both substrings and calculate the number of remotions that we did to get the score.

### Complexity:

- Time complexity: $O(N)$

- Space complexity: $O(N)$