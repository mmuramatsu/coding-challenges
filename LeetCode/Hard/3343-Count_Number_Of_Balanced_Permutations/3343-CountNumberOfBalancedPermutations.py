class Solution(object):
    def countBalancedPermutations(self, num):
        mod = 10**9 + 7
        n = len(num)
        num = list(map(int, num))
        total = sum(num)

        # The total sum needs to be divisible by 2, otherwise is impossible to have sum(oddPart) == sum(evenPart)
        if total & 1:  # total % 2 != 0
            return 0

        factorial = [1] * (n + 1)
        inv = [1] * (n + 1)
        invFact = [1] * (n + 1)

        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i % mod
        for i in range(2, n + 1):
            inv[i] = mod - (mod // i) * inv[mod % i] % mod
        for i in range(1, n + 1):
            invFact[i] = invFact[i - 1] * inv[i] % mod

        target = total // 2
        halfLen = n // 2

        # dp[s][k] = number of ways to choose k digits with a sum s
        dp = [[0] * (halfLen + 1) for _ in range(target + 1)]

        dp[0][0] = 1
        digits = [0] * 10

        # Iterate through each digit 0-9
        for d in num:
            digits[d] += 1

            for i in range(target, d - 1, -1):
                for j in range(halfLen, 0, -1):
                    dp[i][j] = (dp[i][j] + dp[i - d][j - 1]) % mod

        ans = dp[target][halfLen]

        # Multiply by the number of permutations of the first half and the second half
        ans = ans * factorial[halfLen] % mod * factorial[n - halfLen] % mod

        # Divide by the factorials of the counts of each digit to account for repetitions
        for d in digits:
            ans = ans * invFact[d] % mod

        return ans


a = Solution()
print(a.countBalancedPermutations("123"))
print(a.countBalancedPermutations("112"))
print(a.countBalancedPermutations("12345"))
