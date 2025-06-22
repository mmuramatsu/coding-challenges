class Solution:
    # Diff array and prefix-sum - Optimzed version
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)

        # The borders diff[l] and diff[r+1] are maked with -1 and 1, respectively.
        for l, r in queries:
            diff[l] -= 1
            diff[r + 1] = 1

        ps = 0

        for i in range(n):
            ps += diff[i]
            if nums[i] + ps > 0:
                return False

        return True

    # Diff array and prefix-sum
    def isZeroArray1(self, nums: list[int], queries: list[list[int]]) -> bool:
        n = len(nums)
        diff = [0] * n

        # The borders diff[l] and diff[r+1] are maked with -1 and 1, respectively.
        for l, r in queries:
            diff[l] -= 1
            if r + 1 < n:
                diff[r + 1] = 1

        # Prefix sum to fast apply the whole interval on diff
        # For a query [0,2] -> diff[0] = -1 and diff[3] = 1
        # Prefix-sum:
        #   Before: [-1,0,0,1]
        #   After : [-1,-1,-1,0]
        for i in range(1, n):
            diff[i] += diff[i - 1]

        for i in range(n):
            if nums[i] + diff[i] > 0:
                return False

        return True


a = Solution()
print(a.isZeroArray(nums=[1, 0, 1], queries=[[0, 2]]))
print(a.isZeroArray(nums=[4, 3, 2, 1], queries=[[1, 3], [0, 2]]))
print(
    a.isZeroArray(
        nums=[6, 9],
        queries=[
            [1, 1],
            [1, 1],
            [0, 1],
            [1, 1],
            [1, 1],
            [1, 1],
            [1, 1],
            [1, 1],
            [1, 1],
            [1, 1],
            [1, 1],
            [0, 1],
        ],
    )
)
