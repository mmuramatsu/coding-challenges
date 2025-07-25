class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0

        while n != 1:
            ans += n // 2
            n = (n // 2) + (n % 2)

        return ans


a = Solution()
print(a.numberOfMatches(7))
print(a.numberOfMatches(14))
