class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        """
        Given a list `nums`, an integer `key` and an integer `k`, our task is to
        make a list with the index `i` of `nums` for which there exists at least
        one `j` such that `abs(i - j) <= k` and `nums[j] == key`.

        This problem can be solved by two nested loops comparing all elements,
        but we can solve this problem with a more efficient approach. In
        essence, to solve this problem, we just need to know where the `key`
        values are positioned, because all elements that are around this
        element, in a maximum distance of `k` will be part of our answer.

        For example, if we have `nums = [10,20,30,40,50]`, `key = 40` and
        `k = 1`, the answer will be `[2,3,4]`. So, in `i = 3` we have
        `nums[i] = 40 = key`, the interval that will be part of the answer is
        [i - k, i + k + 1[. To avoid the edge case we need to ajust the interval
        as [max(0, i - k), min(n - 1, i + k) + 1[, where `n` is the length of
        `nums`.

        The only problem with this is that we can have repetitions in the
        answer array if we have overlapping intervals for different `i`. To
        solve this we can use the previous right end as the limit for the left
        end of the next founded key. For example, if we have
        `nums = [10,20,40,40,50]`, `key = 40` and `k = 1`, we have two
        occurencies of `key` value in  `i = 2` and `i = 3`, which gives us two
        overlapping intervals, [1,4[ and [2,5[, respectively. If we use the
        right end of the first occurency (`i + k + 1 = 4`) as the left end of
        the next key, we have the intervals [1,4[ and [4,5[, which give us the
        right answer `[1,2,3,4]`.

        So, let `left` and `right` be the left and right endpoints of the range,
        respectively, and let `right` be initialized to 0, we have:
            `left = max(right, i - k)`
            `right = min(n - 1, i + k) + 1`
        """
        ans = []
        n = len(nums)

        right = 0

        for i in range(n):
            if nums[i] == key:
                left = max(right, i - k)
                right  = min(n - 1, i + k) + 1
                for idx in range(left, right):
                    ans.append(idx)

        return ans


a = Solution()
print(a.findKDistantIndices(nums = [3,4,9,1,3,9,5], key = 9, k = 1))
print(a.findKDistantIndices(nums = [2,2,2,2,2], key = 2, k = 2))