class Solution:
    def differenceOfSums1(self, n: int, m: int) -> int:
        num1 = num2 = 0

        for i in range(n + 1):
            if i % m != 0:
                num1 += i
            else:
                num2 += i

        print(f"{num1} {num2}")

        return num1 - num2

    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = num2 = 0

        mult = 0

        # The the multiples of m.
        while mult + m <= n:
            mult += m
            num2 += mult

        # The sum of all numbers from [0,n] minus the multiples of m.
        # The sum of the integers from [0,n] is defined as the sum of the terms
        # of an arithmetic progression with increment 1.
        num1 = (n * (n + 1) // 2) - num2
        return num1 - num2


a = Solution()
print(a.differenceOfSums(n=10, m=3))
print(a.differenceOfSums(n=5, m=6))
print(a.differenceOfSums(n=5, m=1))
