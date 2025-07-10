class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: list[int], endTime: list[int]
    ) -> int:
        # Adding the `eventTime` to the end of `startTime` and `0` to `endTime` to count the borders free time
        # Also, this make it easy to calculate the free times as we basically shifted `endTime` elements, which makes
        # `startTime[i] - endTime[i]` the gap of two events.
        startTime = startTime + [eventTime]
        endTime = [0] + endTime

        n = len(startTime)
        gaps = [startTime[i] - endTime[i] for i in range(n)]

        left = 0
        max_free_time = 0

        # The free time of the first window
        curr_free_time = sum(gaps[:k])

        for right in range(k, n):
            curr_free_time += gaps[right]
            max_free_time = max(max_free_time, curr_free_time)
            curr_free_time -= gaps[left]
            left += 1

        return max_free_time


a = Solution()
print(a.maxFreeTime(eventTime=5, k=1, startTime=[1, 3], endTime=[2, 5]))
print(a.maxFreeTime(eventTime=10, k=1, startTime=[0, 2, 9], endTime=[1, 4, 10]))
print(
    a.maxFreeTime(eventTime=5, k=2, startTime=[0, 1, 2, 3, 4], endTime=[1, 2, 3, 4, 5])
)
