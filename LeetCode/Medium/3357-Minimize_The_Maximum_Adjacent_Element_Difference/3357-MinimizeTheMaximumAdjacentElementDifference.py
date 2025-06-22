class Solution:
    def minDifference(self, nums: list[int]) -> int:
        n = len(nums)

        def check(limit):
            return True

        left = 0
        # Don't know yet
        right = 10**9
        ans = right

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


a = Solution()
print(a.minDifference(nums=[1, 2, -1, 10, 8]))
print(a.minDifference(nums=[-1, -1, -1]))
print(a.minDifference(nums=[-1, 10, -1, 8]))
