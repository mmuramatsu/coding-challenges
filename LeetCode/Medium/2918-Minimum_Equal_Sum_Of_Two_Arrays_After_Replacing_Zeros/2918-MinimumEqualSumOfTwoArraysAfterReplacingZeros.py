class Solution:
    def minSum(self, nums1: list[int], nums2: list[int]) -> int:
        zeros_1 = sum([1 for x in nums1 if x == 0])
        zeros_2 = sum([1 for x in nums2 if x == 0])

        min_max1 = sum(nums1) + zeros_1
        min_max2 = sum(nums2) + zeros_2

        """
        print(sum_1, sum_2)
        print(zeros_1, zeros_2)

        print(max_1, max_2)
        print(min_max1, min_max2)
        """

        if (zeros_1 == 0 and min_max1 < min_max2) or (
            zeros_2 == 0 and min_max2 < min_max1
        ):
            return -1

        return min_max1 if min_max1 > min_max2 else min_max2


a = Solution()
print(a.minSum(nums1=[1, 0, 0, 0], nums2=[2, 0]))
print(a.minSum(nums1=[3, 2, 0, 1, 0], nums2=[6, 5, 0]))
print(a.minSum(nums1=[2, 0, 2, 0], nums2=[1, 4]))
print(a.minSum(nums1=[0, 7, 28, 17, 18], nums2=[1, 2, 6, 26, 1, 0, 27, 3, 0, 30]))
