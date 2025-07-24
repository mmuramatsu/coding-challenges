# Problem: 2163. Minimum Difference in Sums After Removal of Elements (HARD)

## Problem statement:

Given an integer array `nums` of size `3 * n`, we are allowed to remove `n` elements of `nums`. The remaining `2 * n` will be separated in two equal parts, first and second. The **difference in sums** of the two parts is denoted as `sum_first - sum_second`. Our task is to find the minimum **difference in sums** possible.

## Intuition:

To find the minimum **difference in sums** possible we need to minimize the `sum_first` and maximize the `sum_second`. So, the idea is, in some way, remove the greatest values that will be part of the first part and at the same time remove the smallest values from the second part.

To make this we're going to use two Heap Queues. To remove the elements from the first part, we're going to use a **Max Heap** as we need to the greatest elements to be removed. For the second we need the smallest values first, so a **Min Heap** is what we need.

But what will be the strategy to pop elements from each Heap? Let's take a look in an example, let `nums = [2, 3, 1, 8, 5, 4]`. As it said by the problem's statement, the size of this array is `3 * n`. Let's add some bars separate this array in three parts.

    [2 3 | 1 8 | 5 4]

Looking at this it's easy to see that the first part will be formed by some of the first `2 * n` elements as we can only remove `n` elements. For example, if we remove `2` and `3`, the first part will be `1` and `8`. Any combinations of removal will form a first part with `n` number from `[2, 3, 1, 8]`. Similarly, the second part will be formed by `n` elements from the last `2 * n` elements.

#### This problem is asking us to find the optimal way to split the `nums` array in two and find the `n` smallest values of the first part and the `n` greatest values of the second part.

There's a limited way to split the array in two, let's see all the possibilities. I'll going to represent as `"|"` a point of possible split.

    (1) [2 3 | 1 8 5 4]
    (2) [2 3 1 | 8 5 4]
    (3) [2 3 1 8 | 5 4]

In the first one, the first part is already valid (has `n` elements) and is `sum_first = 2 + 3 = 5`, the second part has `2 * n` elements, so using a Min Heap, we will remove the `n` smallest ones, giving us `sum_second = 8 + 5 = 13`. So the difference will be `-8`.

In (2), the first part has more than `n` elements, so we need to remove until we have `n`. In this case, using a Max Heap, we going to remove `3`, giving us `sum_first = 2 + 1 = 3`. As for the second part, we will remove `4`, giving us `sum_second = 8 + 5 = 13`. The difference will be `-10`.

Finally, the (3) way to split. The first part is not valid, so we need to remove elements until we has only `n`. We're going to remove `8` and `3`, giving us `sum_first = 2 + 1 = 3`. The second part is already valid, so we have `sum_second = 5 + 4 = 9`. The difference will be `-6`.

So, in this example the minimum difference possible is `-10`, getting by spliting the array right in the middle.

The idea to solve this is try all ways of spliting and find the minimum, just like we did.

## Approach

Let `left` be a Max Heap and `right` a Min Heap. We will initialize this two heaps with the first `n` elements and the last `n` elements, repectively.

We also will create two arrays `sum_first` and `sum_second`, which will store the sum of each part at each step. We will initialize this two arrays with the sum of the current `left` and `right` heaps.

Next step is to run a for loop from `n` to `2 * n`. Each iteration we will push and pop an item from `left` (adding a new element and removing the maximum). We also going to append the sum of this new heap that we have (`sum_first[-1] - left.pop() + nums[i]`). At the end of this we have in `sum_first` all the sum for each possible split.

At the same loop we can calculate the sum of the second part. We just need to maintain a `j` variable that runs backwards in the interval `[n, 2*n)`. To do this, in every iteration we do `j = (3*n - 1 - i)`. So in each iteration, we push and pop an element from `right` and update the `sum_second` (`sum_second[-1] - right.pop() + nums[j]`). At the end of the loop, we have in `sum_second` all the possible sum for the second part, but backwards. We need to reverse to match the sum of the first part.

The answer of this problem will be the minimum difference between `sum_first[i] - sum_second[i]`, which can be easily done by a `map` function:

`min(map(lambda x, y: x - y, sum_first, sum_second[::-1]))`

### Complexity:
- Time complexity: $O(N \ \log N)$
    - creating `left` and `right`: $O(N)$;
    - heapify takes: $O(\log N)$;
    - the main loop does $2 \cdot N$ Heap operations, which give us $O(N \ \log N)$;
    - mapping the result: $O(N)$.

- Space complexity: $O(N)$
    - `left`: $O(N)$;
    - `right`: $O(N)$;
    - `sum_first`: $O(N)$;
    - `sum_second`: $O(N)$;
    - other variables: $O(1)$.