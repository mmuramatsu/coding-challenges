class Solution:
    def tribonacci1(self, n: int) -> int:
        dp = [0] * 38

        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]

    def tribonacci(self, n: int) -> int:
        minus_1 = 1
        minus_2 = 1
        minus_3 = 0

        for i in range(3, n + 1):
            minus_1, minus_2, minus_3 = minus_1 + minus_2 + minus_3, minus_1, minus_2

        return minus_1


a = Solution()
print(a.tribonacci(4))
print(a.tribonacci(25))
print(a.tribonacci(37))
