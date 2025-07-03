class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7
        groups = []
        n = len(word)

        count = 1

        for i in range(1, n):
            if word[i - 1] == word[i]:
                count += 1
            else:
                groups.append(count)
                count = 1

        groups.append(count)

        total = 1

        for size in groups:
            total *= size % MOD

        if len(groups) >= k:
            return total

        prefix_sum = [1] * k

        for size in groups:
            dp = [0] * k

            for length in range(1, k):
                dp[length] = prefix_sum[length - 1]

                if length - size - 1 >= 0:
                    dp[length] -= prefix_sum[length - size - 1] % MOD

            prefix_sum = [0] * k

            for i in range(1, k):
                prefix_sum[i] = prefix_sum[i - 1] + dp[i]

        return (total - prefix_sum[k - 1]) % MOD


a = Solution()
print(a.possibleStringCount(word="aabbccdd", k=7))
print(a.possibleStringCount(word="aabbccdd", k=8))
print(a.possibleStringCount(word="aaabbb", k=3))
