from math import lcm


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def count_ugly(k):
            """
            Counts the number of ugly numbers (divisible by a or b or c)
            that are less than or equal to k using the Principle of Inclusion-Exclusion.
            """
            # k // a: Counts numbers <= k divisible by a.
            # k // b: Counts numbers <= k divisible by b.
            # k // c: Counts numbers <= k divisible by c.
            # If we just added these, numbers divisible by two or three of a, b, c would be overcounted.

            # k // lcm_ab: Counts numbers <= k divisible by both a and b. We subtract this to correct the overcounting.
            # k // lcm_ac: Counts numbers <= k divisible by both a and c. We subtract this to correct the overcounting.
            # k // lcm_bc: Counts numbers <= k divisible by both b and c. We subtract this to correct the overcounting.
            # Now, numbers divisible by all three (a, b, and c) have been added three times and subtracted three times, resulting in a count of zero for them. We need to add them back once.

            # k // lcm_abc: Counts numbers <= k divisible by a, b, and c. We add this back to correct the undercounting.
            return (
                (k // a)
                + (k // b)
                + (k // c)
                - (k // lcm_ab)
                - (k // lcm_ac)
                - (k // lcm_bc)
                + (k // lcm_abc)
            )

        lcm_ab = lcm(a, b)
        lcm_ac = lcm(a, c)
        lcm_bc = lcm(b, c)
        lcm_abc = lcm(a, lcm(b, c))

        low = 1
        high = 2 * 10**9  # A sufficiently large upper bound
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if count_ugly(mid) >= n:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans


a = Solution()
print(a.nthUglyNumber(n=3, a=2, b=3, c=5))  # 4
print(a.nthUglyNumber(n=4, a=2, b=3, c=4))  # 6
print(a.nthUglyNumber(n=5, a=2, b=11, c=13))  # 10
