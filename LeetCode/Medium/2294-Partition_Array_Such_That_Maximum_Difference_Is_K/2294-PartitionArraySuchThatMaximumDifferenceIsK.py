class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        """
        Given an integer array `nums` and an integer `k`, our task is to find
        how many arrays we need to subdivide the `nums` array, where the
        difference between the maximum and minimum values in each subsequence is
        at most k.

        Whenever we need to minimize the difference between the elements of an
        array, it is a good idea to sort the array.

        As we have all the elements sorted the key point to solve this problem
        is that we need to always know which number is the first value of the
        current subsequence. The first element of the current subsequence always
        will be the minimum `min` of that subsequence, so the maximum value that
        can fit in this subsequence is  `min + k`.

        So, first of all, we sort the array, then we define `ans = 1`
        (the constraint ensures that there is always at least one valid
        subsequence.) and `max_value = nums[0] + k`, which is the maximum value
        possible for the first subsequence. Then, for each `num` in `nums` we
        check if `num > max_value`, if it is, we need to form a new subsequence
        (`ans += 1`) and update our `max_value`.

        Time Complexity: O(N log N)
        Space Complexity: O(N)
        """
        nums.sort()

        ans = 1
        max_value = nums[0] + k

        for num in nums:
            if num > max_value:
                ans += 1
                max_value = num + k

        return ans


a = Solution()
print(a.partitionArray(nums=[3, 6, 1, 2, 5], k=2))
print(a.partitionArray(nums=[1, 2, 3], k=1))
print(a.partitionArray(nums=[2, 2, 4, 5], k=0))
