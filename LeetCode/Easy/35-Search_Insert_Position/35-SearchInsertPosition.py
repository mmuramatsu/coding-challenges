class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        ans = -1

        while start <= end:
            mid = (start + end) // 2
            if target > nums[mid]:
                ans = mid
                start = mid + 1
            else:
                end = mid - 1

        return ans + 1


a = Solution()
print(a.searchInsert(nums=[1, 3, 5, 6], target=5))
print(a.searchInsert(nums=[1, 3, 5, 6], target=2))
print(a.searchInsert(nums=[1, 3, 5, 6], target=7))
print(a.searchInsert(nums=[1, 3, 5, 6], target=0))
