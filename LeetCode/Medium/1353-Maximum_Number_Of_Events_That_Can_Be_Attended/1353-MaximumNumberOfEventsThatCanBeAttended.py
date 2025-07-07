import heapq


class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        n = len(events)
        count = 0
        events.sort(key=lambda x: x[0])

        day = 0
        j = 0
        available = []

        while j < n or available:

            if not available and j < n:
                day = max(day, events[j][0])

            # Add potential events to the available
            while j < n and events[j][0] == day:
                heapq.heappush(available, events[j][1])
                j += 1

            # Remove invalid events
            while available and available[0] < day:
                heapq.heappop(available)

            # pick the best event from avaliable
            if available:
                heapq.heappop(available)
                count += 1
                day += 1

        return count


a = Solution()
print(a.maxEvents(events=[[1, 2], [2, 3], [3, 4]]))
print(a.maxEvents(events=[[1, 2], [2, 3], [3, 4], [1, 2]]))
print(a.maxEvents(events=[[1, 2], [2, 2], [3, 3], [3, 4], [3, 4]]))
print(a.maxEvents(events=[[1, 2], [1, 2], [3, 3], [1, 5], [1, 5]]))
