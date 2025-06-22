from collections import defaultdict


def countCompleteSubarrays(nums: list[int]) -> int:
    total_unique = len(set(nums))
    n = len(nums)
    res = 0

    subarray_freq = defaultdict(int)
    unique = 0
    left = 0

    for right in range(n):
        subarray_freq[nums[right]] += 1
        if subarray_freq[nums[right]] == 1:  # distinct number found.
            unique += 1

        while unique == total_unique:
            # All next subarrays are complete if the previous one is.
            res += n - right

            # Shrinking the window, by removing the nums[left] from the frequency dict
            subarray_freq[nums[left]] -= 1

            # If is true, the new subarray ({nums[left+1], ..., nums[right]}) are not complete.
            if subarray_freq[nums[left]] == 0:
                unique -= 1

            # Move left end forward
            left += 1

    return res


print(countCompleteSubarrays([1, 3, 1, 2, 2]))
print(countCompleteSubarrays([5, 5, 5, 5]))
