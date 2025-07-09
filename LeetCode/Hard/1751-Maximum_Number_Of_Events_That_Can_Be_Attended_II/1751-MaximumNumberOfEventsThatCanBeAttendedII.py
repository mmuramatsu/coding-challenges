import bisect


class Solution:
    # DP botton-up + Precomputate binary search. Beats 71.77%.
    def maxValue(self, events: list[list[int]], k: int) -> int:
        n = len(events)
        events.sort(key=lambda x: x[0])
        start_day = [s for s, _, _ in events]
        next_event = [bisect.bisect_right(start_day, events[e][1]) for e in range(n)]

        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for event_idx in range(n - 1, -1, -1):
            for k_reminder in range(1, k + 1):
                skip = dp[event_idx + 1][k_reminder]
                attend = (
                    dp[next_event[event_idx]][k_reminder - 1] + events[event_idx][2]
                )

                dp[event_idx][k_reminder] = max(skip, attend)

        return dp[0][k]

    # DP top-down + Precomputate binary search. Beats 85.16%.
    def maxValue1(self, events: list[list[int]], k: int) -> int:
        n = len(events)
        memo = [[-1] * (k + 1) for _ in range(n)]
        events.sort(key=lambda x: x[0])
        start_day = [s for s, _, _ in events]
        next_event = [bisect.bisect_right(start_day, events[e][1]) for e in range(n)]

        def solve(event_idx, k):
            if k == 0 or event_idx >= n:
                return 0

            if memo[event_idx][k] != -1:
                return memo[event_idx][k]

            # Skip event
            skip = solve(event_idx + 1, k)

            # Attend event
            attend = solve(next_event[event_idx], k - 1) + events[event_idx][2]

            memo[event_idx][k] = max(skip, attend)

            return memo[event_idx][k]

        return solve(0, k)

    # DP top-down solution. Beats 65.93%.
    def maxValue1(self, events: list[list[int]], k: int) -> int:
        n = len(events)
        memo = [[-1] * (k + 1) for _ in range(n)]
        events.sort(key=lambda x: x[0])
        start_day = [s for s, _, _ in events]

        def solve(event_idx, k):
            if k == 0 or event_idx >= n:
                return 0

            if memo[event_idx][k] != -1:
                return memo[event_idx][k]

            # Skip event
            skip = solve(event_idx + 1, k)

            # Attend event
            next_event = bisect.bisect_right(start_day, events[event_idx][1])
            attend = solve(next_event, k - 1) + events[event_idx][2]

            memo[event_idx][k] = max(skip, attend)

            return memo[event_idx][k]

        return solve(0, k)


a = Solution()
print(a.maxValue(events=[[1, 2, 4], [3, 4, 3], [2, 3, 1]], k=2))
print(a.maxValue(events=[[1, 2, 4], [3, 4, 3], [2, 3, 10]], k=2))
print(a.maxValue(events=[[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], k=3))
