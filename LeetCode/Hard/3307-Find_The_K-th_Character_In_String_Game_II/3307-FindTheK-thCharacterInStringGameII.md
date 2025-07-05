# Problem: 3307 - Find the K-th Character in String Game II (HARD)

## Problem statement

Bob and Alice are playing a game where Alice starts with the string `s = "a"` and will perform transformations in that string. There's two transformation possible to be applied to `s`. The first one is to append a copy of `s`. The second one is generate a new string by changing each character in `s` to it's next character in the English alphabet, and append it to the original `s`. Given an integer `k` and an integer array `operations`, our task is to return the `k`-th character of `s` after the transformations, in which the type of each transformation is defined by `operations[i]`, where `0` represent the first type of transformations and `1` the second type.

## Solution 2 - Divide and conquer:

An important detail of this problem is that the length of `s` doubles after each tranformation. We can use this to avoid the simulation and focus on how many times the `k`-th character was shifted.

First, we calculate the smallest power of $2$, `current_len`, that is **greater than** the 0-indexed `k`. This `current_len` represents the length of the string after the necessary number of transformations (say, `t`) such that the `k`-th character is guaranteed to exist within it. We initialize `current_len = 1` and multiply it by $2$ until `current_len > k`."

During this loop, we also will define a variable `t` that will count how many transformations `s` need to suffer to get to the corrent length. Starting `t = 0`, in each iteration we increment `t` by one.

To make it easy to solve this problem, let's suposse that the `operations` array are full of `1`s. In other words, all the transformations applied to `s` are the second type, where generate a new string, shift the characters of `s` and append to `s`.

For example, if we are looking for the `k = 5`, we have `current_len = 8`, which lead us to the string `"abbcbccd"`.

Now, we're going to check how many shifts the character that we're looking for have passed. We're going to ues a divide and conquer strategy to find in which part of the string the `k`-th character falls. The idea is, if `k` falls within the first half of the generated string after `t` transformations, then the `k`-th character is just the `k`-th character of the string generated after `t - 1` transformations. If `k` falls within the second half of the generated string after `t` transformations, then `k` is a character that was shifted in the last transformation.

For example, in the string `s = "abbcbccd"` and `k = 5`. First we do `k = k - 1` to make `k` a 0-indexed value. If we split the string in two (`t - 1` transformations and the last transformation), we have `"abbc"` and `"bccd"` and update `current_len //= 2 = 4`. In this scenario, with `k = 4`, we verify that `k` falls in the second half, meaning that `k` is some character of the first half shifted one time. We now update `k = k - current_len = 0`.

Let's do it again for the string `"abbc"`. First we split, `"ab"` and `"bc"`. We verify that `k` now is on the first half, meaning that the `k` haven't been shifted in this transformation. Let's head to the next tranformation, `"ab"`, will be `"a"` and `"b"`. Now, `k` falls again on the first half, so it haven't been shifted again. We get to the original string, so we stop.

Now that we know how to check if the `k`-th character have been part of the last transformation or not we can add the `operations` array to the problem. If `k` falls within the first half, nothing change, we still don't need to apply a shift to the final character as `k` is not part of the last transformation. If `k` falls in the second half on the other hand, there's two options. The first is if `operations[t] = 1`, the last tranformation is the one that require a shift, so we shift. The second is when `operations[t] = 0`, even if `k` is part of the last tranformation, is a transformation that don't require a shift, so we don't shift in this case. In each iteration we decrement `t` to match the last transformation applied.

Remembering that, every time we shift the final char, we need to take care is final character don't pass `"z"`, if it does, we cycle the final character back to `"a"`.

### Complexity:
- Time complexity: $O(log \; k)$

- Space complexity: $O(1)$