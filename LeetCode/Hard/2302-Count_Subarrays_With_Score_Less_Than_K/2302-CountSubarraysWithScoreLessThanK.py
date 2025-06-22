class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        ans = 0
        left = 0

        # Will act as a prefix sum.
        current_sum = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            # Until find a valid nums[left...right] array, increment left.
            while current_sum * (right - left + 1) >= k:
                current_sum -= nums[left]
                left += 1

            # If nums[left...right] is valid, then all nums[left+1...right], nums[left+2...right], etc, are valid.
            ans += right - left + 1

        return ans


a = Solution()
print(a.countSubarrays([1, 1, 1, 0], 5))  # output = 7
print(a.countSubarrays([1, 1, 1], 5))  # output = 5
print(a.countSubarrays([2, 1, 4, 3, 5], 10))  # output = 6
print(a.countSubarrays([4, 3, 5], 11))  # output: 3
