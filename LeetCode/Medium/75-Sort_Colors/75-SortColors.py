class Solution:
    # Counting sort
    def sortColors1(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]

        for num in nums:
            count[num] += 1

        j = 0

        for i in range(len(count)):
            while count[i] != 0:
                nums[j] = i
                j += 1
                count[i] -= 1

    # Dutch National Flag Alogrithm - Pointers
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        low = mid = 0
        high = n - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1

        print(nums)


a = Solution()
print(a.sortColors([2, 0, 2, 1, 1, 0]))
print(a.sortColors([2, 0, 1]))
