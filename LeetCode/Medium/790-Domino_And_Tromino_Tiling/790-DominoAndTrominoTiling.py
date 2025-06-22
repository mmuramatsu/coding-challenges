class Solution:
    def numTilings1(self, n: int) -> int:
        MOD = 10**9 + 7
        ans = [1, 1, 2, 5, 11]

        if n <= 4:
            return ans[n]

        for i in range(5, n + 1):
            ans.append((2 * ans[i - 1] + ans[i - 3]) % MOD)

        return ans[n]

    def numTilings2(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [1, 1]
        im = [0, 0]

        for i in range(2, n + 1):
            im.append((dp[i - 2] + im[i - 1]) % MOD)
            dp.append((dp[i - 1] + dp[i - 2] + 2 * im[i - 1]) % MOD)

        return dp[n]

    def numTilings(self, n: int) -> int:
        if n <= 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 5

        prev_prev = 1
        prev = 2
        cur = 5

        for i in range(4, n + 1):
            cur, prev, prev_prev = 2 * cur + prev_prev, cur, prev

        return cur % (10**9 + 7)


a = Solution()
# print(a.numTilings(1))
# print(a.numTilings(2))
# print(a.numTilings(3))
print(a.numTilings(4))
print(a.numTilings(5))
print(a.numTilings(30))  # 312342182
