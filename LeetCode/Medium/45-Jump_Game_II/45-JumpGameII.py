class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)

        dp = [float("inf")] * n
        dp[n - 1] = 0

        for i in range(n - 2, -1, -1):
            dp[i] = 1 + min(dp[i : i + nums[i] + 1])

        return dp[0]


a = Solution()
print(a.jump([2, 3, 1, 1, 4]))
print(a.jump([2, 3, 0, 1, 4]))
