# Problem: 3330 - Find the Original Typed String I (EASY)

## Problem statement

Given a string `word` that may have some repeted characters in sequence due to a typo of Alice. Our task is to find the total number of possible original strings that Alice might have intended to type.

## Intuition

In simple terms, we basically need to count the repetitions in a sequence of some character. So, starting from the second character of `word`, if the previous character is equal to the current one, we increment our count. It's important to make our count start with $1$, which represent the string without typos.