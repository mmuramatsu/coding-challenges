# Problem: 3439 - Reschedule Meetings for Maximum Free Time I (MEDIUM)

## Problem statement:

It's given to us an integer `eventTime` denoting the duration of an event from `t = 0` to `t = eventTime`. We also receive two integer arrays `startTime` and `endTime`, which representing non-overlapping meetings, where each meeting start at `startTime[i]` and ends in `endTime[i]`. Finally, we also receive an integer `k`, which represents the number of meeting that we can reschedule.

Our task is to find the largest free time by reschedule `k` meetings, maintaining the same order, duration and non-overlapping time between the meetings.

## Intuition:

Basically, this problem wants to know how much free time we have in a window of length `k`, because imagine that we have three meetings and the free time between the first and the second is `3` and the free time between the second and the third is `2`. To maximize the free time in sequence we can stick all three meetings so that one meeting happens after the other without a break. By doing that we going to have a free time in sequence of `5`, which is equal to the previous free time that we have but splitted.

So, the idea is to calculate the gaps between the meetings and then using a sliding window of length `k + 1` (k meetings between these k+1 gaps), and find the maximum free time finded in this window.

There are two cases that we need to take care, which is the case when we have a free time before the first meeting and after the last meeting. To solve this we can manipulate the input arrays to make that explicit in the gaps calculation.

First, we're going to append to `startTime` the total event time `eventTime` and preppend to `endTime` the start of the event `0`. By doing that, we can calculate the gaps at the beginning and end of the event if happens to have. Also, we make it easier to calculate the gaps, we simply do `startTime[i] - endTime[i]` to get the gap value.

Why this happen? When we add a new value at the beginning of the `endTime`, we basically shift the values to the left, so `startTime[0]` represent the start time of the first meeting, while `endTime[0]` is the start of the event, so `startTime[0] - endTime[0]`, will give us the gap before the first meeting. The `startTime[1]` is the start time of the second meeting, while `endTime[1]` is the end time of the first meeting, so `startTime[1] - endTime[1]` is the gap between the first and second meeting, which is correct.

Let `gaps` be the array of length `n` that store all the gaps between the meetings, including the gap before and after the meetings. Let `max_free_time` be the variable that will store the maximum free time seem and `curr_free_time` be the variable that store the current window free time. First, we're going to calculate the sum of the `k` gaps and save in `curr_free_time`. We're going to start a for loop from `k` to `n`, which will represent the `right` end of our sliding window. The left end of our window starts in `left = 0`.

The process is:
- add `gaps[right]` to `curr_free_time`;
- calculate the maximum, `max_free_time = max(max_free_time, curr_free_time)`;
- remove `gaps[left]` from `curr_free_time`;
- update left end.

At the end of this loop, `max_free_time` will have the answer of the problem.

### Complexity:
- Time complexity: $O(N)$
    - Append and prepend: $O(N)$;
    - Construct `gaps` array: $O(N)$;
    - Summing the first window can be $O(N)$;
    - Sliding window part: $O(N)$.

- Space complexity: $O(N)$
    - `gaps` table: $O(N)$.