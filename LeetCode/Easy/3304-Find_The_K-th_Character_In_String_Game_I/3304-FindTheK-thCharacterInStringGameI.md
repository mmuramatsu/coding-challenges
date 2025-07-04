# Problem: 3304 - Find the K-th Character in String Game I (EASY)

## Problem statement

Bob and Alice are playing a game where Alice starts with the string `s = "a"` and will perform transformations in that string. The transformation applied to `s` is generate a new string by changing each character in `s` to it's next character in the English alphabet, and append it to the original `s`. Given an integer `k`, our task is to return the `k`-th character of `s` after the transformations.

## Solution 1 - Simulation:

The simplest way to solve this problem is to simulate the transformations and generate all the string.

We just need a loop that will stop when we have a string of length greater or equal to `k`. Inside that loop we will generate the new string by loop through each character of `s` and increment its ASCII value by $1$. At the end of this we append to `s` the new string.

When this all ends, we just return the `k`-th character.

### Complexity:
- Time complexity: $O(k)$

- Space complexity: $O(k)$

## Solution 2 - Divide and conquer:

An important detail of this problem is that the length of `s` doubles after each tranformation. We can use this to avoid the simulation and focus on how many times the `k`-th character was shifted.

The idea is simple. First, we calculate the smallest power of $2$, `current_len`, that is **greater than** the 0-indexed `k`. This `current_len` represents the length of the string after the necessary number of transformations (say, `t`) such that the `k`-th character is guaranteed to exist within it. We initialize `current_len = 1` and multiply it by $2$ until `current_len > k`."

For example, if we are looking for the `k = 5`, we have `current_len = 8`, which lead us to the string `"abbcbccd"`.

Now, we're going to check how many shifts the character that we're looking for have passed. We're going to ues a divide and conquer strategy to find in which part of the string the `k`-th character falls. The idea is, if `k` falls within the first half of the generated string after `t` transformations, then the `k`-th character is just the `k`-th character of the string generated after `t - 1` transformations. If `k` falls within the second half of the generated string after `t` transformations, then `k` is a character that was shifted in the last transformation.

For example, in the string `s = "abbcbccd"` and `k = 5`. First we do `k = k - 1` to make `k` a 0-indexed value. If we split the string in two (`t - 1` transformations and the last transformation), we have `"abbc"` and `"bccd"` and update `current_len //= 2 = 4`. In this scenario, with `k = 4`, we verify that `k` falls in the second half, meaning that `k` is some character of the first half shifted one time. We now update `k = k - current_len = 0`.

Let's do it again for the string `"abbc"`. First we split, `"ab"` and `"bc"`. We verify that `k` now is on the first half, meaning that the `k` haven't been shifted in this transformation. Let's head to the next tranformation, `"ab"`, will be `"a"` and `"b"`. Now, `k` falls again on the first half, so it haven't been shifted again. We get to the original string, so we stop. The number of shifts that the `k`-th character suffer is $1$, so our return is `chr(ord("a") + 1)`.

### Complexity:
- Time complexity: $O(log \; k)$

- Space complexity: $O(1)$

## Solution 3 - Math:

There's an interesting way to solve this based on the previous solution. Let's do the dry run for `k = 7`. First decrement `k` to match the 0-indexed of our string, so `k = 6`. We start with the string `"abbcbccd"`. In this situation, `k` falls in the second half of the string, so shift $1$ due to the `t = 3` tranformation. Next, for the string `"abbc"` and `k = 2`. This time `k` falls on the second half again, so shift $1$ due to the `t = 2` transformation. Lastly, for the string `"ab"` and `k = 0`. Now, `k` falls in the first half, so, we don't shift in for `t = 1` transformation. The result is `"a" + 2`.

If we check what is the binary representation of $6$, we have `110`. An interestingly thing is that the number of `1`s in the binary representation of $6$ is equal of the number of shifts needed to find the `k`-th character of  `s`.

But why this happend? We know that the length of the string `s` after `t` tranformations is $2^{t}$. In our example, we have `t = 3`, and we tracked that for `k = 7`, we shifted in the tranformations `t = 3` and `t = 2` and we don't shift for `t = 1`, and this match exactly the bit representation of the number $6$. For the most significant digit, $2^3$, we have `1` and for `t = 3` we shift. For the second bit, $2^2$, we have `1` and for `t = 2` we shift. For the least significant bit, $2^1$, we have `0` and for `t = 1` we didn't shifted.

The next table presents the result for `k = 0` to `k = 7`.


k (0-indexed) |Binary of k|	Path |	Character |	Number of Shifts|
| ---------- | ---------- | ---------- | ---------- | ---------- |
0 (a) |	000	| First half, First half, First half	| a	| 0 |
1 (b)|	001	| First half, First half, **Second half**	| b	| 1 |
2 (b)|	010	| First half, **Second half**, First half	| b	| 1 |
3 (c)|	011	| First half, **Second half**, **Second half**	| c	| 2 |
4 (b)|	100	| **Second half**, First half, First half	| b	| 1 |
5 (c)|	101	| **Second half**, First half, **Second half**	| c	| 2 |
6 (c)|	110	|**Second half**, **Second half**, First half	| c	| 2 |
7 (d)|	111	|**Second half**, **Second half**, **Second half**	| d	| 3

So, the answer for our problem is `chr(ord("a") + (k - 1).bit_count())`.

### Complexity:
- Time complexity: $O(1)$

- Space complexity: $O(1)$