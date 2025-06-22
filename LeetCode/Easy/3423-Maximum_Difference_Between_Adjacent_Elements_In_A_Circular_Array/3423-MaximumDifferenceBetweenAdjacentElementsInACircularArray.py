class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        """
        Our task is to find the maximum absolute difference between two adjacent
        numbers in `nums`.

        We just need to calculate for each adjacent numbers. In this case, we
        have a circular array, so we can start our `ans` value with the absolute
        difference of the edges by doing `ans = abs(nums[0] - nums[-1])`.
        """
        ans = abs(nums[0] - nums[-1])

        for i in range(1, len(nums)):
            diff = abs(nums[i] - nums[i - 1])

            ans = ans if ans > diff else diff

        return ans


a = Solution()
print(a.maxAdjacentDistance(nums=[1, 2, 4]))
print(a.maxAdjacentDistance(nums=[-5, -10, -5]))
