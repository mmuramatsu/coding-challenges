# Problem: 1957 - Delete Characters to Make Fancy String (EASY)

## Problem statement:

Given a string `s`, our task is to make `s` a **fancy string**, in which is a string where no three consecutive characters are the same.

## Intuition:

We can solve this problem using a simple for loop. We're going to iterate through each character of `s` counting how many repeated character we have in sequence by comparing the current one with the previous one. If the count is less than 3, we add the current character to the answer, otherwise, we just skip.
If the current character is different than the previous one, we reset the count to 1.

The first character will always be part of the answer, so we can start by adding the first character to the answer. So, our for loop can iterate from the second character to the end.

We can make a simple shortcut for some test cases by adding a condition at the beginning, checking if the length of the string is less than 3. If it is, we can simply return `s`, as a string with length less than 3 characters can't have three repeted characters or more.

### Complexity:
- Time complexity: $O(N)$

- Space complexity: $O(1)$