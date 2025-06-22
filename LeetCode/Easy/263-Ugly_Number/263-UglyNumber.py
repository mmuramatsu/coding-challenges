class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True

        for i in [2, 3, 5]:
            while n > 0 and n % i == 0:
                n //= i

        return n == 1


a = Solution()
print(a.isUgly(6))
print(a.isUgly(1))
print(a.isUgly(14))

for i in range(100):
    print(f"{i}: {a.isUgly(i)}")
