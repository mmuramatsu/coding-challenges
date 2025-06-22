class Solution:
    def buildArray1(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n

        for i in range(n):
            ans[i] = nums[nums[i]]

        return ans

    def buildArray(self, nums: list[int]) -> list[int]:
        return [nums[nums[i]] for i in range(len(nums))]


a = Solution()
print(a.buildArray([0, 2, 1, 5, 3, 4]))
print(a.buildArray([5, 0, 1, 2, 3, 4]))
