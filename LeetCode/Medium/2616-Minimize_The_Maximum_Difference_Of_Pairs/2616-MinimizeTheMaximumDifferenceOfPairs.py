class Solution:
    # Binary-search solution. Beats 85.43%.
    def minimizeMax(self, nums: list[int], p: int) -> int:
        """
        Given an array of integers `nums` and an integer `p`, our task is to
        choose `p` pairs such that the maximum difference among all the pairs is
        minimized.

        This is a little bit confusing so, let's change the perspective. Given
        an array `nums`, can we form `p` pairs where the difference among all of
        then is less or equal than `x`? If the answer is Yes, then, we can also
        make `p` pairs where the difference is less than `x'`, where `x' > x`.
        We basically want o minimize this `x` to be the minimum as possible, and
        that will be our answer. So instead of find the pairs that can form the
        minimum maximum difference, we find which minimum maximum difference we
        can form. If we can't form, we need to try a greater number.

        Based on that, it's intuitive to think about Binary-search, where the
        left end is 0 and the right end is the greater number of `nums`. First
        of all, as we want to pick the number in a optimal way based of the
        difference of pairs of indexes, we can sort the array, so the difference
        always will be minimal.

        We're going to define a helper function that will verify if it's
        possible to form `p` pairs with difference less or equal to `x`. We
        simply will iterate through the array comparing if
        `nums[i] - nums[i-1] <= x` (we don't need to get the absolute value as
        the array is sorted we are dealing with non-negative differences.). If
        it's True, then we increase the count. We also need to increase `i` by
        one, as the constraints says that we can't repeat indexes among the
        pairs. When this loop ends, we return True if `count >= p`, otherwise,
        False.

        In our binary-search structure, our `mid` term will act as the `x`
        explained before. So, we calculate the `mid` and verify if it's possible
        to form the pairs using the helper function. If it is, meaning that any
        number greater than this `mid` is also possible, so we need to look at
        the left part of the window. So, save this as our temporary answer and
        update `right = mid - 1`. If it's not possible to form the pairs, then
        we need to look at the right part of the window, by doing
        `left = mid + 1`.

        At the end of the binary-search we have the answer.
        """
        nums.sort()
        n = len(nums)

        def is_possible(x):
            i = 1
            count = 0

            while i < n:
                if nums[i] - nums[i - 1] <= x:
                    count += 1
                    i += 1

                i += 1

            return count >= p

        left = 0
        right = nums[-1] - nums[0]
        ans = 0

        while left <= right:
            mid = (right + left) // 2

            if is_possible(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


a = Solution()
print(a.minimizeMax(nums=[10, 1, 2, 7, 1, 3], p=2))
print(a.minimizeMax(nums=[4, 2, 1, 2], p=1))
