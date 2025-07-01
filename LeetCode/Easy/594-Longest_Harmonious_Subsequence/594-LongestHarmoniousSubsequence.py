from collections import Counter


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        freq = Counter(nums)
        ans = 0

        for k, v in freq.items():
            if freq[k + 1] != 0:
                ans = ans if ans > freq[k] + freq[k + 1] else freq[k] + freq[k + 1]

        return ans

    def findLHS1(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)

        ans = 0
        j = 0

        for i in range(n):
            while j < n and nums[j] - nums[i] <= 1:
                j += 1

            if nums[i] != nums[j - 1]:
                ans = max(ans, j - i)

        return ans


a = Solution()
print(a.findLHS(nums=[1, 3, 2, 2, 5, 2, 3, 7]))
print(a.findLHS(nums=[1, 2, 3, 4]))
print(a.findLHS(nums=[1, 1, 1, 1]))
