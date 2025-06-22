class Solution:
    """Queue version
    def countSubarrays(self, nums: list[int], k: int) -> int:
        ans = 0

        max_value = max(nums)
        pos_queue = []

        for i in range(len(nums)):
            if nums[i] == max_value:
                pos_queue.append(i)

                if len(pos_queue) > k:
                    pos_queue.pop(0)

            if len(pos_queue) == k:
                ans += pos_queue[0] + 1

        return ans
    """

    """ List version
    def countSubarrays(self, nums: list[int], k: int) -> int:
        ans = 0
        max_value = max(nums)
        max_indices = []
        start_index = 0

        for i in range(len(nums)):
            if nums[i] == max_value:
                max_indices.append(i)

            while len(max_indices) - start_index > k:
                start_index += 1

            if len(max_indices) - start_index == k:
                ans += max_indices[start_index] + 1

        return ans
    """

    """
    def countSubarrays(self, nums: list[int], k: int) -> int:
        ans = 0
        max_value = max(nums)
        freq = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == max_value:
                freq += 1

            while freq >= k:
                if nums[left] == max_value:
                    freq -= 1

                left += 1

            ans += left

        return ans
    """

    # Reverse count approach. Count the cases where it has less than k then subtract the total subarrays (n * (n + 1) // 2) by the the total calculated.
    def countSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_value = max(nums)
        count = 0
        left = 0
        max_count = 0

        for right in range(n):
            if nums[right] == max_value:
                max_count += 1

            while max_count >= k:
                if nums[left] == max_value:
                    max_count -= 1
                left += 1

            count += right - left + 1

        return (n * (n + 1) // 2) - count


a = Solution()
print(a.countSubarrays([1, 3, 2, 3, 3], 2))
print(a.countSubarrays([1, 4, 2, 1], 3))
