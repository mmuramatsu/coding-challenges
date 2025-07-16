class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        odd = 0
        even = 0
        alternate_even = 0
        alternate_odd = 0
        next_even = True
        next_odd = True
        for num in nums:
            if num & 1:
                # Odd
                odd += 1
                if next_odd:
                    alternate_odd += 1
                    next_odd = False

                if not next_even:
                    alternate_even += 1
                    next_even = True
            else:
                # Even
                even += 1

                if next_even:
                    alternate_even += 1
                    next_even = False

                if not next_odd:
                    alternate_odd += 1
                    next_odd = True

        return max(even, odd, alternate_even, alternate_odd)


a = Solution()
print(a.maximumLength(nums=[1, 2, 3, 4]))
print(a.maximumLength(nums=[1, 2, 1, 1, 2, 1, 2]))
print(a.maximumLength(nums=[1, 3]))
