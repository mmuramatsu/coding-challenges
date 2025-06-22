class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.prefix_sum = [nums[0]]

        for i in range(1, len(nums)):
            self.prefix_sum.append(self.prefix_sum[i - 1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return (
            self.prefix_sum[right]
            if left == 0
            else self.prefix_sum[right] - self.prefix_sum[left - 1]
        )


a = NumArray([-2, 0, 3, -5, 2, -1])
print([-2, 0, 3, -5, 2, -1])
print(a.prefix_sum)
print(a.sumRange(0, 2))
print(a.sumRange(2, 5))
print(a.sumRange(0, 5))
