import heapq


class Solution:

    # Using only a set (Beats 10.77%)
    def nthUglyNumber1(self, n: int) -> int:
        ugly_values = set([1])
        count = 0

        while count != n:
            ans = min(ugly_values)
            ugly_values.remove(ans)
            count += 1

            ugly_values.add(2 * ans)
            ugly_values.add(3 * ans)
            ugly_values.add(5 * ans)

        return ans

    # Using a combination of set an heapq (Beats 45.41%)
    def nthUglyNumber2(self, n: int) -> int:
        ugly_values = set([1])
        queue = [1]
        count = 0

        while count != n:
            ans = heapq.heappop(queue)
            count += 1

            if 2 * ans not in ugly_values:
                heapq.heappush(queue, 2 * ans)
                ugly_values.add(2 * ans)
            if 3 * ans not in ugly_values:
                heapq.heappush(queue, 3 * ans)
                ugly_values.add(3 * ans)
            if 5 * ans not in ugly_values:
                heapq.heappush(queue, 5 * ans)
                ugly_values.add(5 * ans)

        return ans

    # Using DP (Beats 50.22%)
    def nthUglyNumber3(self, n: int) -> int:
        ugly_values = [0] * n
        ugly_values[0] = 1

        primes = [2, 3, 5]
        index_next_UN = [0, 0, 0]
        next_UN = [2, 3, 5]

        for i in range(1, n):
            next_number = min(next_UN)
            ugly_values[i] = next_number

            for i in range(3):
                if next_number == next_UN[i]:
                    index_next_UN[i] += 1
                    next_UN[i] = ugly_values[index_next_UN[i]] * primes[i]

        return ugly_values[-1]

    # Using DP optimized (Beats 98.58%)
    def nthUglyNumber(self, n: int) -> int:
        ugly_values = [0] * n
        ugly_values[0] = 1

        index_UN1, index_UN2, index_UN3 = 0, 0, 0
        next_UN1, next_UN2, next_UN3 = 2, 3, 5

        for i in range(1, n):
            next_number = min(next_UN1, next_UN2, next_UN3)
            ugly_values[i] = next_number

            if next_number == next_UN1:
                index_UN1 += 1
                next_UN1 = ugly_values[index_UN1] * 2
            if next_number == next_UN2:
                index_UN2 += 1
                next_UN2 = ugly_values[index_UN2] * 3
            if next_number == next_UN3:
                index_UN3 += 1
                next_UN3 = ugly_values[index_UN3] * 5

        return ugly_values[-1]


a = Solution()
print(a.nthUglyNumber(10))
print(a.nthUglyNumber(1))
