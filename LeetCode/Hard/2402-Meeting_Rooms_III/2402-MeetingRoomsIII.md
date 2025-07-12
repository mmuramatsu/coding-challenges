# Problem: 2402 - Meeting Rooms III (HARD)

## Problem statement:

Given an integer `n` representing the number of rooms available and an array `meetings`,  where `meetings[i] = [starti, endi]` means that a meeting will be held during the half-closed time interval `[starti, endi)`. To book a meeting to a room, we need to follow the following rules:
- Each meeting will take place in the unused room with the lowest number;
- If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting;
- When a room becomes unused, meetings that have an earlier original start time should be given the room.

Our taks is to find the room that held the most meetings and return.

## Intuition:

The problem says that a "meeting will take place in the unused room with the lowest number", with that, we know that we need a way to fast find a unused room, because it's unfeasible to run a whole array to find an empty room every time. If we are interest in the room with the lowest number we can use a Min Heap to store the rooms that are free to use, so every time we need a room, we pop an element from the Heap which is the minimum element of the Heap. Let's call this Min heap as `free_rooms`.

If there's no free rooms, the next meeting will take place in the room that ends first, or we can say the minimum end time of the meeting that are happening, which lead us to another Min Heap. We can use another Min Heap to store the tuple `(endTime, room)`, where `endTime` is the end time of the meeting held by the room `room`. So, every time we need to know which meeting will end first, we just pop an element from this Heap and we will know which room will be free to use next. Let's call this Min Heap as `occupied_rooms`.

It's important to sort the meeting based on the `startTime`, so we can run the meetings in time order.

The algorithm to solve this is, for each meeting:
- Remove already ended meetings and free up rooms;
- Book the current meeting to some rooms;
    - If there are free rooms, simply book to the one with the lowest number;
    - If there are no free room, find the meeting with minimum ending time in `occupied_rooms` and book the current meeting to that room with the delay;
- increse the count of the room used in this iteration.

## Approach:

First we will define `free_rooms`, which initially will have all rooms from `0` to  `n - 1`, `occupied_rooms` will be initially empty and `rooms_count`, which will count how many meetings each rooms helded, will start full of zeros.

The idea to solve this consist 2 steps, for each meeting `m`:
- while `occupied_rooms` is not empty and `occupied_rooms.top() <= m.startTime`, we pop elements from `occupied_rooms` and push the empty room to `free_rooms`;
- Book a meeting;
    - if `free_rooms` is not empty, pop an element from `free_rooms` and push to `occupied_rooms` the tuple `(m.endTime, room)`;
    - if `free_rooms` is empty, pop an elemento from `occupied_rooms` and push a new tuple to `occupied_rooms`, `(m.endTime + (prev.endTime + m.startTime), room)`;
- increase the count of `rooms_count[room] += 1`.

Finally, return the index of the maximum of `rooms_count`.

### Complexity:
Let $N$ be the number of rooms and $M$ the number of meetings.

- Time complexity: $O(M \ log \ M)$
    - Sorting: $O(M \ log \ M)$;
    - Construct `free_rooms` and `rooms_count` array: $O(N)$;
    - Each meeting leads to a few heap operations (e.g., push to occupied, pop from free/occupied), so $O(M \ log \ M)$;
    - Find the maximum: $O(N)$.

- Space complexity: $O(N)$
    - `free_rooms` array: $O(N)$;
    - `occupied_rooms`: $O(N)$;
    - `rooms_count`: $O(N)$.
    - other variables: $O(1)$