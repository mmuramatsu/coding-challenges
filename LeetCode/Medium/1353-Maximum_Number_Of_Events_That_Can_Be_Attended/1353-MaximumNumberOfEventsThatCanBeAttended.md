# Problem: 1353 - Maximum Number of Events That Can Be Attended (MEDIUM)

## Problem statement

Given an array of arrays `events`, where `events[i] = [startDayi, endDayi]`, so every event starts in `startDayi` and ends in `endDayi`, in which `startDayi <= endDayi`. Our task is to find the maximum number of events we can attend. We can only attend one event per day.

## Intuition:

First of all, it's important to sort the `events` array based on `startDay`. In that way it will be easy so choose which event to go at each `day`.

We can say that the events can be in three different states based on `day`.
- `day < saturDay`: the event has not started yet, so the status can be `unseen`;
- `startDay <= day <= endDay `: the event is happening now and is a possible event to go, so the status can be `available`;
-  `day > endDay`: the event already end, the status can be `invalid`.

The key point of this problem is the strategy to pick the best event of overlaped events. If we have, for example, two events `a = [1,1]`, and `b = [1,2]`, which one should we pick first? In that case we need to pick the event `a` at `day = 1` and `b` at `day = 2`. We can say then, that we always want to pick the one that has the earliest `endDay` first.

Based on that we can use a Min Heap to always get the event with the minimum `endDay` from the available ones. The idea can be splited in four steps:
- Update the current day to `day = max(day, events[j][0])`;
- While `events[j][0] == day`, we add the `events[j][1]` to our Min Heap (add available);
- While  `minHeap.top() < day` we remove elements from our Min Heap (remove invalids);
- Pick the best event to go at this `day` by pop an element from our Min Heap (increment the count).

We're going to repeat this until we process all events in `events` and in our Min Heap.

### Complexity:

- Time complexity: $O(N \ log \ N)$
    - We take $O(N \ log \ N)$ for sorting;
    - All heap operations (push and pop) are done once for the `N` elements, so we have $O(N \ log \ N)$.

- Space complexity: $O(N)$
    - In the worst case, all events start at the same day, so we need to store all events in our Min Heap, which will lead to an $O(N)$ space complexity.