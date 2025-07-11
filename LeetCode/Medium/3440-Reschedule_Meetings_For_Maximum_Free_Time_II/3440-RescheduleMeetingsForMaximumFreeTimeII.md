# Problem: 3440 - Reschedule Meetings for Maximum Free Time II (MEDIUM)

## Problem statement:

It's given to us an integer `eventTime` denoting the duration of an event from `t = 0` to `t = eventTime`. We also receive two integer arrays `startTime` and `endTime`, which representing non-overlapping meetings, where each meeting start at `startTime[i]` and ends in `endTime[i]`.

Our task is to find the most free time by rescheduling only `1` meeting, keeping the meeting duration and non-overlapping meetings

## Intuition:

Let's analyze what is happening if we change a meeting from the original place. All meeting are surrounded by free time, let's say gaps. If another meeting start right before the previous, we can say that the gap is equal to 0.

Based on that, let `left` and `right` be the gaps on the left and right of a meeting `m`, respectively. There're two possible scenarios for a `m`. If we move `m` to some gap different of `left` and `right`, the total free time in this case will be the sum of `left` and `right` and the duration of `m`. The other scenario is when there's no other gap that can fit `m`, besides `left` and `right`. In this scenario, the best we can do is to move `m` to some endpoint and merge `left` and `right` into one largest free time.

Let `max_free_time` be the variable that will store the maximum free time seem and `curr_free_time` be the variable that store the current free time. So, the algorithm will be, for each meeting `m`:
- search for a gap that can fit `m` that are different than `left` and `right`;
- if we find, the `curr_free_time` will be `left + m.duration + right`;
- if we didn't find, `curr_free_time` will be `left + right`;
- update `max_free_time` to `max(max_free_time, curr_free_time)`.

## Approach:

First of all, we're going to append to `startTime` the total event time `eventTime` and preppend to `endTime` the start of the event `0`. By doing that, we can calculate the gaps at the beginning and end of the event if happens to have. Also, we make it easier to calculate the gaps, we simply do `startTime[i] - endTime[i]` to get the gap value.

Why this happen? When we add a new value at the beginning of the `endTime`, we basically shift the values to the left, so `startTime[0]` represent the start time of the first meeting, while `endTime[0]` is the start of the event, so `startTime[0] - endTime[0]`, will give us the gap before the first meeting. The `startTime[1]` is the start time of the second meeting, while `endTime[1]` is the end time of the first meeting, so `startTime[1] - endTime[1]` is the gap between the first and second meeting, which is correct.

Let `gaps` be the array that store the gaps between meetings. To easily find gaps that can fit `m`, we can sort `gaps` and store the last `3` elements in other array called `sorted_gaps` (instead of sorting, we can use a loop to find the top 3 gaps, it will be $O(N)$).

Why `3` elements? The idea is that a meeting `m` can fit in any gap that are greater than or equal to the duration of `m`, so the best candidates of a gap that can fit `m` is the greater gaps in `gaps`. To find the maximum, first we need to find some gap different from `left` and `right`, so if we have 3 elements to compare, we guarantee that we can find at least one that are different from `left` and `right`.

We also will calculate the meetings duration by doing `endTime[i] - startTime[i - 1]` and save in `meetings[i]`.

Let `j` be the index that mark the gaps around `m` and `gaps[j - 1]` and `gaps[j]` be `left` and `right`, respectively. So for each `m` in `meetings`, we will search in `sorted_gaps` a gap to fit `m` that are different from `left` and `right`. If we find, we update `curr_free_time = gaps[j - 1] + duration + gaps[j]`. Otherwise, `curr_free_time = gaps[j - 1] + gaps[j]`.

Then we update `max_free_time = max(max_free_time, curr_free_time)`.

At the end of this loop we will have the maximum contiguous free time after rescheduling one meeting in `max_free_time`.

### Complexity:
- Time complexity: $O(N \ log \ N)$
    - Append and prepend: $O(N)$;
    - Construct `gaps` array: $O(N)$;
    - Sorting: $O(N \ log \ N)$;
    - Processing each meeting: $O(N)$;
    - Finding the gap to fit the meeting: $O(1)$.

- Space complexity: $O(N)$
    - `gaps` array: $O(N)$;
    - `sorted_gaps`: $O(N)$;
    - `meetings`: $O(N)$.
    - other variables: $O(1)$