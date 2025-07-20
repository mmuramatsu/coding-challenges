class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        longest = 0

        for num in nums:
            curr = num % k

            for prev in range(k):
                dp[curr][prev] = dp[prev][curr] + 1
                longest = max(longest, dp[curr][prev])

        return longest


a = Solution()
print(a.maximumLength(nums=[1, 2, 3, 4, 5], k=2))
print(a.maximumLength(nums=[1, 4, 2, 3, 1, 4], k=3))
