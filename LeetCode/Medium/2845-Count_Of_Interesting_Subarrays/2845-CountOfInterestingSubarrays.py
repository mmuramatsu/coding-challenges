from collections import defaultdict


class Solution:
    def countInterestingSubarrays_brute(
        self, nums: list[int], modulo: int, k: int
    ) -> int:
        res = 0

        for left in range(len(nums)):
            cnt = 0
            for right in range(left, len(nums)):
                if nums[right] % modulo == k:
                    cnt += 1

                if cnt % modulo == k:
                    res += 1

        return res

    def countInterestingSubarrays(self, nums: list[int], modulo: int, k: int) -> int:
        res = 0

        prefix_sum_list = [1 if nums[0] % modulo == k else 0]

        for i in range(1, len(nums)):
            prefix_sum_list.append(
                prefix_sum_list[i - 1] + (1 if nums[i] % modulo == k else 0)
            )

        remainder_counts = defaultdict(int)
        remainder_counts[0] = 1

        for r in range(len(nums)):
            target_remainder = (prefix_sum_list[r] - k + modulo) % modulo
            if target_remainder in remainder_counts:
                res += remainder_counts[target_remainder]

            current_remainder = prefix_sum_list[r] % modulo
            remainder_counts[current_remainder] += 1

        print(remainder_counts)
        return res


a = Solution()
print(a.countInterestingSubarrays([3, 2, 4], 2, 1))
print(a.countInterestingSubarrays([3, 1, 9, 6], 3, 0))
print(a.countInterestingSubarrays([1, 2, 1, 2], 2, 1))

# print(a.countInterestingSubarrays_brute([1, 2, 1, 2], 2, 1))
