class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        ans = set()
        n = len(digits)

        # Test all possible 3-digit case
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or i == k or j == k:
                        continue

                    num = digits[i] * 100 + digits[j] * 10 + digits[k]

                    if 99 < num <= 998 and not num & 1:
                        ans.add(num)

        return len(ans)


a = Solution()
print(a.totalNumbers([1, 2, 3, 4]))
print(a.totalNumbers([0, 2, 2]))
print(a.totalNumbers([6, 6, 6]))
print(a.totalNumbers([1, 3, 5]))
