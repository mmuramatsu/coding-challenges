class Solution:
    def countSubarrays_brute(self, nums: list[int], minK: int, maxK: int) -> int:
        ans = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                min_value, max_value = min(nums[i:j]), max(nums[i:j])

                if min_value == minK and max_value == maxK:
                    print(nums[i:j])
                    ans += 1

        return ans

    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        ans = 0

        min_pos = -1
        max_pos = -1
        invalid = -1

        for r in range(len(nums)):
            if nums[r] == maxK:
                max_pos = r

            if nums[r] == minK:
                min_pos = r

            if nums[r] > maxK or nums[r] < minK:
                invalid = r

            # print(min_pos, max_pos, invalid)

            if max_pos > invalid and min_pos > invalid:
                ans += (max_pos if max_pos < min_pos else min_pos) - invalid

        return ans


a = Solution()
# print(a.countSubarrays_brute([1, 3, 5, 2, 7, 5], 1, 5))
# print(a.countSubarrays_brute([5, 1, 3, 4, 0, 7, 8, 5, 5, 1], 1, 5))
# print(a.countSubarrays([1, 1, 1, 1], 1, 1))
print(a.countSubarrays_brute([4, 5, 1, 3, 7, 5, 5, 1, 2], 1, 5))
print(a.countSubarrays([4, 5, 1, 3, 7, 5, 5, 1, 2], 1, 5))
