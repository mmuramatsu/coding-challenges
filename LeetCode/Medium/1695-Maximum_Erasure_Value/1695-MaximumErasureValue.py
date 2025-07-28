class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        elements = set([nums[0]])
        sum_elements = nums[0]
        ans = nums[0]

        left = 0

        for right in range(1, n):
            if nums[right] in elements:
                while nums[left] != nums[right]:
                    sum_elements -= nums[left]
                    elements.remove(nums[left])
                    left += 1

                sum_elements -= nums[left]
                elements.remove(nums[left])
                left += 1

            elements.add(nums[right])
            sum_elements += nums[right]
            ans = max(ans, sum_elements)

        return ans


a = Solution()
print(a.maximumUniqueSubarray(nums=[4, 2, 4, 5, 6]))
print(a.maximumUniqueSubarray(nums=[5, 2, 1, 2, 5, 2, 1, 2, 5]))
