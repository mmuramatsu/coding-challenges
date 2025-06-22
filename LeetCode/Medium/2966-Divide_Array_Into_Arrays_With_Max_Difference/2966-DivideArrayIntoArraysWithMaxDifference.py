class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        """
        Given an array of integers `nums` and a integer `k`, our task is to
        contruct an 2D array `ans`, where `ans[i]` is an array of length 3 where
        the difference between any two elements in this array is less than or
        equal to `k`.

        Every time we need to minimize the difference between elements of an
        array, one good idea is to sort the array.

        We need to contruct arrays of lenght 3 where the difference don't get
        greater than `k`, so basically, the difference between the maximum value
        and the minimum of this array can't be greater than `k`. We don't need
        to care about the middle value as we already sort the `nums` array, so
        the value of the middle element will be between the max and the min.

        So, to solve this problem, we can loop through the `nums` array from `0`
        to `n` incrementing `i` by 3 every iteration. In each iteration we check
        if `nums[i + 2] - nums[i] <= k` (max - min <= k). If it is, then we
        append the list with this 3 elements (`nums[i]`, `nums[i+1]`,
        `nums[i+2]`) in our `ans`. Otherwise, it's impossible to form an `ans`
        array that follows the conditions, so we return `[]`.
        """
        nums.sort()
        n = len(nums)

        ans = []

        for i in range(0, n, 3):
            if nums[i + 2] - nums[i] <= k:
                ans.append(nums[i : i + 3])
            else:
                return []

        return ans

    def divideArray1(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)

        i = 0
        ans = [[0] * 3 for _ in range(n // 3)]
        cur_list = 0
        cur_idx = 0

        while i < n:
            if cur_idx != 0 and nums[i] <= max_value:
                ans[cur_list][cur_idx] = nums[i]
                cur_idx += 1

                if cur_idx == 3:
                    cur_list += 1
                    cur_idx = 0
            elif cur_idx == 0:
                ans[cur_list][cur_idx] = nums[i]
                max_value = nums[i] + k
                cur_idx += 1
            else:
                return []

            i += 1

        return ans


a = Solution()
print(a.divideArray(nums=[1, 3, 4, 8, 7, 9, 3, 5, 1], k=2))
print(a.divideArray(nums=[2, 4, 2, 2, 5, 2], k=2))
print(
    a.divideArray(nums=[4, 2, 9, 8, 2, 12, 7, 12, 10, 5, 8, 5, 5, 7, 9, 2, 5, 11], k=14)
)
