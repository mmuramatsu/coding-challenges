MOD = 10**9 + 7
powers = [1] * 10**5
for i in range(1, 10**5):
    powers[i] = (powers[i - 1] * 2) % MOD


class Solution:
    # Two pointers with optimized window + pre-calculation out of function solution. Beats 99.89%.
    def numSubseq(self, nums: list[int], target: int) -> int:
        n = len(nums)
        count = 0
        nums.sort()

        left = 0
        right = n - 1

        while left <= right:
            if nums[left] + nums[right] <= target:
                count += powers[right - left]
                left += 1
            else:
                right -= 1

        return count % MOD

    # Two pointers with optimized window + pre-calculation solution. Beats 92.14%.
    def numSubseq1(self, nums: list[int], target: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        count = 0
        nums.sort()

        powers = [1] * n
        for i in range(1, n):
            powers[i] = (powers[i - 1] * 2) % MOD

        left = 0
        right = n - 1

        while left <= right:
            if nums[left] + nums[right] <= target:
                count += powers[right - left]
                left += 1
            else:
                right -= 1

        return count % MOD

    # Two pointers + pre-calulation solution. Beats 79.80%.
    def numSubseq2(self, nums: list[int], target: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        count = 0
        nums.sort()

        powers = [1] * n
        for i in range(1, n):
            powers[i] = (powers[i - 1] * 2) % MOD

        j = n - 1

        for i in range(n):
            while j >= i and nums[i] + nums[j] > target:
                j -= 1

            if i > j:
                if nums[i] * 2 <= target:
                    aux = 1
                else:
                    aux = 0
            else:
                aux = powers[j - i]

            count += aux

        return count % MOD

    # Two point solution. Beats 28.74%
    def numSubseq1(self, nums: list[int], target: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        count = 0
        nums.sort()

        j = n - 1

        for i in range(n):
            while j >= i and nums[i] + nums[j] > target:
                j -= 1

            if i > j:
                if nums[i] * 2 <= target:
                    aux = 1
                else:
                    aux = 0
            else:
                aux = 2 ** (j - i)

            count += aux

        return count % MOD


a = Solution()
print(a.numSubseq(nums=[3, 5, 6, 7], target=9))
print(a.numSubseq(nums=[3, 3, 6, 8], target=10))
print(a.numSubseq(nums=[2, 3, 3, 4, 6, 7], target=12))
print(a.numSubseq(nums=[1, 2, 3, 4, 5, 6], target=5))
