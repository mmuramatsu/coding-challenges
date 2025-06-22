class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly_values = [0] * n
        ugly_values[0] = 1

        index_next_UN = [0] * len(primes)
        next_UN = [x for x in primes]

        lenght = len(primes)

        for i in range(1, n):
            next_number = min(next_UN)
            ugly_values[i] = next_number

            for i in range(lenght):
                if next_number == next_UN[i]:
                    index_next_UN[i] += 1
                    next_UN[i] = ugly_values[index_next_UN[i]] * primes[i]

        return ugly_values[-1]


a = Solution()
print(a.nthSuperUglyNumber(n=12, primes=[2, 7, 13, 19]))  # 32
print(a.nthSuperUglyNumber(n=1, primes=[2, 3, 5]))  # 1
