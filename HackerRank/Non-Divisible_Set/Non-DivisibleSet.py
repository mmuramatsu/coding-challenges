from collections import defaultdict


class Solution:
    def nonDivisibleSubset(self, s: list[int], k: int) -> int:
        """
        Intuition:
            If two numbers have remainders r1 and r2 such that (r1 + r2) % k == 0,
            then we cannot include both numbers in our non-divisible subset.

            Case for remainder 0: If we include one number with remainder 0,
            adding any other number with remainder 0 will result in a sum divisible by k.
            So, we can include at most one.

            Case for remainder k/2 (if k is even): If we include one number with remainder k/2,
            adding another number with the same remainder will result in a sum divisible by k.
            So, we can include at most one.

            For the other remainders, we consider pairs (i, k-i).
            If a number has remainder i, and another has remainder k-i, their sum is divisible by k.
            We can choose to take all numbers with remainder i or all numbers with remainder k-i,
            whichever count is larger.
        """

        # Create a dictionary to store the counts of each remainder modulo k.
        # The key is the remainder (0 to k-1), and the value is the count of numbers in s with that remainder.
        reminder_count = defaultdict(int)

        for num in s:
            reminder_count[num % k] += 1

        size = 0

        # Case for reminder 0
        if reminder_count[0] > 0:
            size += 1

        # Case for reminder k/2
        if not k & 1 and reminder_count[k // 2] > 0:
            size += 1

        # We iterate from 1 up to floor((k-1)/2) to cover all such pairs.
        for i in range(1, (k + 1) // 2):
            size += max(reminder_count[i], reminder_count[k - i])

        return size


a = Solution()
print(a.nonDivisibleSubset([19, 10, 12, 10, 24, 25, 22], 4))
print(a.nonDivisibleSubset([1, 7, 2, 4], 3))
print(a.nonDivisibleSubset([1, 2, 3, 4, 5], 4))
print(a.nonDivisibleSubset([27, 18, 6, 22, 13, 25], 5))
print(a.nonDivisibleSubset([1, 1, 1, 1], 2))
print(a.nonDivisibleSubset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
print(a.nonDivisibleSubset([4, 5, 6, 7], 3))
print(a.nonDivisibleSubset([0, 1, 2], 2))
