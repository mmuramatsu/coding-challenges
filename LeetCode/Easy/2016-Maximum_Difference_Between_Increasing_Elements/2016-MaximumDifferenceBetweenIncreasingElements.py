class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        """
        Given an array `nums`, we need to find the maximum difference
        `nums[j] - nums[i]`, where `i < j`.

        The idea here is to create a variable to keep track of the minimum value
        of the array founded so far. We initialize our `minimum` variable as
        `nums[0]`, and start a for loop of `j` in range [1, len(nums)].

        If `nums[j] > minimum`, then `nums[j] - minimum` is a canditate of
        maximum, so we update our answer. Otherwise, we found a new minimum
        value that can potentially lead use to a greater maximum, so we update
        our `minimum` variable with `nums[j]`.
        """
        ans = -1

        minimum = nums[0]

        for j in range(1, len(nums)):
            if nums[j] > minimum:
                ans = max(ans, nums[j] - minimum)
            else:
                minimum = nums[j]

        return ans


a = Solution()
print(a.maximumDifference(nums=[7, 1, 5, 4]))
print(a.maximumDifference(nums=[9, 4, 3, 2]))
print(a.maximumDifference(nums=[1, 5, 2, 10]))
print(a.maximumDifference(nums=[50, 100, 1, 10]))
