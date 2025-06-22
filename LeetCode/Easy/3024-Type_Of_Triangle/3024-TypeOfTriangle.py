class Solution:
    def triangleType(self, nums: list[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] > nums[2]:
            if nums[0] == nums[1] and nums[0] == nums[2]:
                return "equilateral"

            if nums[0] == nums[1] or nums[0] == nums[2] or nums[1] == nums[2]:
                return "isosceles"

            return "scalene"

        return "none"


a = Solution()
print(a.triangleType([3, 3, 3]))
print(a.triangleType([3, 4, 5]))
print(a.triangleType([3, 3, 5]))
print(a.triangleType([2, 7, 7]))
