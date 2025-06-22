class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        ans = 0

        for i in range(2, len(nums)):
            if nums[i - 2] + nums[i] == nums[i - 1] / 2:
                print(nums[i - 2], nums[i - 1], nums[i])
                ans += 1

        return ans


a = Solution()
a.countSubarrays([1, 2, 1, 4, 1])
