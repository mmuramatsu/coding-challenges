from collections import Counter


class Solution:
    # One state DP
    def canPartition(self, nums: list[int]) -> bool:
        tot = sum(nums)

        if tot & 1:
            return False

        half_tot = tot // 2
        dp = [False] * (half_tot + 1)
        dp[0] = True

        for num in nums:
            for i in range(half_tot, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[half_tot]

    # Memorization approach (TLE)
    def canPartition1(self, nums: list[int]) -> bool:
        tot = sum(nums)
        if tot & 1:
            return False
        half_tot = tot // 2
        n = len(nums)
        initial_freq = Counter(nums)

        memo = {}

        def dp(freq_tuple, cur_sum):
            if cur_sum == half_tot:
                return True
            if cur_sum > half_tot:
                return False

            if (freq_tuple, cur_sum) in memo:
                return memo[(freq_tuple, cur_sum)]

            freq = Counter(dict(freq_tuple))

            for k in sorted(freq.keys()):  # Iterate through numbers
                if freq[k] > 0:
                    aux_freq = freq.copy()
                    aux_freq[k] -= 1
                    aux_freq_tuple = tuple(sorted(aux_freq.items()))
                    if dp(aux_freq_tuple, cur_sum + k):
                        memo[(freq_tuple, cur_sum)] = True
                        return True

            memo[(freq_tuple, cur_sum)] = False
            return False

        initial_freq_tuple = tuple(sorted(initial_freq.items()))
        return dp(initial_freq_tuple, 0)


a = Solution()
print(a.canPartition([1, 5, 11, 5]))
print(a.canPartition([1, 2, 3, 5]))
print(a.canPartition([23, 13, 11, 7, 6, 5, 5]))  # True
print(a.canPartition([1, 1]))  # True
print(a.canPartition([6, 14, 19, 10, 17, 10, 8, 15, 16, 1, 12, 4, 9, 2, 15]))  # True
print(a.canPartition([4, 10, 7, 9, 7, 1, 11, 9, 13, 15]))  # True
print(a.canPartition([9, 10, 15, 3, 9, 2, 9, 10, 13, 1]))  # False
print(
    a.canPartition(
        [
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            99,
            97,
        ]
    )
)  # False
