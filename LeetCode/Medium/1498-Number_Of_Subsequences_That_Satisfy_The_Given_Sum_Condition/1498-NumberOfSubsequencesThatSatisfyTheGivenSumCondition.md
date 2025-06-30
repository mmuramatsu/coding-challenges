# Problem: 1498 - Number of Subsequences That Satisfy the Given Sum Condition (MEDIUM)

Given an interger array `nums` and an integer `target`, our task is to find the number of subsequences in which the sum of the maximum and minimum element is less than or equal to `target`.

Since we are looking at subsequences and only care about the maximum and minimum of that subsequence we can sort the array, beacuse in this case the order of the array doesn't matter. With a sorted array, it's a lot easier to find the maximum and minimum.

The idea for solving this problem is to use a two pointers approach. As we have an sorted array we can fix our left pointer and consider as the minimum value of the array. Now we need to find a position for our right pointer, in which `nums[left] + nums[right] <= target` is `True`. We can initialize `right = n - 1`, where `n` is the length of `nums`. We will decrement `right` until we make the condition `True`.

A key point of this problem is the monotonic property of the problem after sorting. For a minimum `nums[left]` we have a maximum possible in `nums[right]`, for a minimum in `nums[left + 1]`, the maximum possible for this can only be found at `nums[right]` or on left of this.

Let's see an example to visualize the solution. Let `nums = [1,2,3,4,5,6]` and `target = 5`. For `left = 0`, the maximum that possible that we can find is `right = 3`. Now, the problem is how we can count the number of subsequences. In this situation the possible subsequences are `{[1], [1,2], [1,3], [1,4], [1,2,3], [1,2,4], [1,3,4], [1,2,3,4]}`, total of $8$ or we can say $2^{right - left}$. The number of possible subsequences for `left = 1` and `right = 2` is $2^{2 - 1} = 2$. For `left = 2`, we can't form a valid subsequence, which means that we also can't form a valid subsequence for any next values. So the total of valid subsequences is $10$.

So, to solve this problem we:
1. sort the array to make it easier to find the maximum and minimum;
2. For each `left` from 0 to `n` as minimum we need to find a maximum `right` starting from `n - 1` to 0 that can satisfy `nums[left] + nums[right] <= target`;
3. Count the number of valid subsequences, which is $2^{right - left}$.

## Optimization 1:

We can use a Binary seach-like approach to optimize the window. We start the `left` point as 0 and the `right` pointer as `n - 1`. Then, `while left <= right` we verify if `nums[left] + nums[right] <= target` is `True`. If it is, we add the $2^{right - left}$ to the `count` and increment `left`. If it's not `True`, then we just decrement `right`. This loop will end when we can't form a valid subsequence with minimum `nums[left]`.

## Optimization 2:

Since we need to calculate $2^x$ multiple times, we can precompute this to avoid recalculating the same value over and over again. We can create a `powers` array with $10^5$ positions and calculate every single value of $2^x$ for $x$ in $[0,10^5]$.

### Performance trick

LeetCode instantiate our solution Class once and then call the solution function for each test case, so we can do the precalculations out of all this. In that way, our code will calculate the powers only once and use the values for each test case, which give us a awesome performance.