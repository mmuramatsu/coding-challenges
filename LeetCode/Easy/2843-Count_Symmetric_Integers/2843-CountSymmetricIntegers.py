class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0

        for i in range(low, high + 1):
            if not ((i > 0 and i < 11) or (i > 99 and i < 1001)):
                num = i
                prefix_sum = [num % 10]
                num //= 10

                while num > 0:
                    prefix_sum.append(
                        num % 10 + prefix_sum[len(prefix_sum) - 1]
                    )  # extract last digit
                    num //= 10

                if (
                    prefix_sum[(len(prefix_sum) // 2) - 1]
                    == prefix_sum[len(prefix_sum) - 1]
                    - prefix_sum[(len(prefix_sum) // 2) - 1]
                ):
                    ans += 1

        return ans


a = Solution()
print(a.countSymmetricIntegers(1, 100))
print(a.countSymmetricIntegers(1200, 1230))
