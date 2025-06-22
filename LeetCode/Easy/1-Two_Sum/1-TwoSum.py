class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        previous = {}

        for i in range(len(nums)):
            if (target - nums[i]) in previous:
                return [previous[target - nums[i]], i]

            previous[nums[i]] = i


a = Solution()
print(a.twoSum(nums=[2, 7, 11, 15], target=9))
print(a.twoSum(nums=[3, 2, 4], target=6))
print(a.twoSum(nums=[3, 3], target=6))
