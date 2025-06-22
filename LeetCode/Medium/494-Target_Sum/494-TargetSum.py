class Solution:
    # Memorization approach
    def findTargetSumWays1(self, nums: list[int], target: int) -> int:
        n = len(nums)

        memo = {}

        def dp(i, cur_sum):
            if i == n:
                return 1 if cur_sum == target else 0

            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)]

            memo[(i, cur_sum)] = dp(i + 1, cur_sum + nums[i]) + dp(
                i + 1, cur_sum - nums[i]
            )

            return memo[(i, cur_sum)]

        return dp(0, 0)

    # Tabulation - 2D state DP
    def findTargetSumWays2(self, nums: list[int], target: int) -> int:
        n = len(nums)
        total_sum = sum(nums)

        dp = [[0] * (2 * total_sum + 1) for _ in range(n)]

        # Initialize the first row based on the first number
        if n > 0:
            dp[0][total_sum + nums[0]] = 1
            dp[0][total_sum - nums[0]] += 1

        for i in range(1, n):
            for j in range(2 * total_sum + 1):
                # Consider adding nums[i]
                prev_sum_add = j - nums[i]
                if 0 <= prev_sum_add <= 2 * total_sum:
                    dp[i][j] += dp[i - 1][prev_sum_add]

                # Consider subtracting nums[i]
                prev_sum_sub = j + nums[i]
                if 0 <= prev_sum_sub <= 2 * total_sum:
                    dp[i][j] += dp[i - 1][prev_sum_sub]

        if abs(target) > total_sum:
            return 0
        return dp[n - 1][target + total_sum]

    # Tabulation - 1D state DP
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total_sum = sum(nums)
        if abs(target) > total_sum:
            return 0

        offset = total_sum
        dp = [0] * (2 * total_sum + 1)
        dp[offset] = (
            1  # Base case: sum of 0 can be achieved in 1 way (empty subset initially)
        )

        for num in nums:
            next_dp = [0] * (2 * total_sum + 1)
            for current_sum_offset in range(2 * total_sum + 1):
                if dp[current_sum_offset] > 0:
                    # Add the current number
                    add_offset = current_sum_offset + num
                    if 0 <= add_offset <= 2 * total_sum:
                        next_dp[add_offset] += dp[current_sum_offset]

                    # Subtract the current number
                    subtract_offset = current_sum_offset - num
                    if 0 <= subtract_offset <= 2 * total_sum:
                        next_dp[subtract_offset] += dp[current_sum_offset]
            dp = next_dp

        return dp[target + offset]


a = Solution()

print(a.findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))
print(a.findTargetSumWays(nums=[1], target=1))
print(a.findTargetSumWays(nums=[1], target=2))
print(a.findTargetSumWays(nums=[1, 0], target=1))  # 2
print(
    a.findTargetSumWays(
        nums=[
            35,
            37,
            9,
            29,
            36,
            0,
            44,
            32,
            44,
            13,
            2,
            37,
            14,
            21,
            41,
            36,
            9,
            23,
            41,
            17,
        ],
        target=42,
    )
)
