# Problem: 1290 - Convert Binary Number in a Linked List to Integer (EASY)

## Problem statement:

Given a `head` of a singly-linked list in which each node has a value `0` or `1`. The linked list holds a binary representation of a number. Our task is to find the decimal representation of the number in the linked list, knowing that the most significant bit in at the head.

## Intuition:

To solve this we just need to run through every single node of the linked list and add to a accumulator each bit that we see. We start our accumulator with `0`, let's say `num`. Starting from the head with a pointer `curr`, for each node we do `num = (num << 1) + curr.val` and go to the next node. We will repet this until we reach `curr == None`.

At the end of this loop we have the decimal representation of the number in the linked list in `num`.

### Complexity:
- Time complexity: $O(N)$

- Space complexity: $O(1)$