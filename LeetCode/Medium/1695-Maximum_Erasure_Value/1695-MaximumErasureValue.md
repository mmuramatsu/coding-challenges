# Problem: 1695 - Maximum Erasure Value (MEDIUM)

## Problem statement:

Given a positive integer array `nums`, our task is to find the subarray with unique elements that has the greatest sum among all subarrays.

## Intuition:

This problem can be solved by a simple Sliding Window approach. The idea is to move the right side of the windows, or we can say, add new elements to the window as long as we have unique elements in the window. When we hit a value that is already in the window, we need to shrink the window, in other words, move left side of the window. We need to shrink, until we remove the repeated element from the window.

One way to always know if we have unique elements is by using a set. When we move the right side of the window, we add this new elements to our set if it's not in the set already. When we move the left side of the window we remove from the set.

We also, need to keep track of the sum of the current window. We just need to add to the sum the new value added to the window and subtract when we remove from the window. The last thing we need to do at the end of each iteration, we need to check if the current sum is greater than the maximum that we had seem in the past.

At the end of this for loop, we have the maximum sum of the subarray with unique elements.

### Complexity:

- Time complexity: $O(N)$

- Space complexity: $O(N)$