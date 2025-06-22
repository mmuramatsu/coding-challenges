class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        prev_prev = 0
        prev = 0

        for i in range(n):
            prev, prev_prev = min(cost[i] + prev, cost[i] + prev_prev), prev

        return min(prev, prev_prev)


a = Solution()
print(a.minCostClimbingStairs([10, 15, 20]))
print(a.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
