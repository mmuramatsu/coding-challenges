class Solution:
    # Binary search approach
    def minZeroArray1(self, nums: list[int], queries: list[list[int]]) -> int:
        n = len(nums)

        def check(k):
            diff = [0] * (n + 1)

            for i in range(k):
                l, r, v = queries[i]
                # The borders diff[l] and diff[r+1] are maked with -1 and 1, respectively.
                diff[l] += v
                diff[r + 1] -= v

            ps = 0

            for i in range(n):
                ps += diff[i]
                if nums[i] > ps:
                    return False

            return True

        # Binary search to find the best k.
        start = 0
        end = len(queries)
        ans = -1

        while start <= end:
            mid = (start + end) // 2

            if check(mid):
                end = mid - 1
                ans = mid
            else:
                start = mid + 1

        return ans

    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        n = len(nums)
        m = len(queries)
        diff = [0] * (n + 1)

        ps = 0
        k = 0

        for i in range(n):
            while nums[i] > ps + diff[i]:
                k += 1

                if k > m:
                    return -1

                l, r, v = queries[k - 1]

                if l <= i <= r or r > i:
                    diff[max(l, i)] += v
                    diff[r + 1] -= v

            ps += diff[i]

        return k


a = Solution()
print(a.minZeroArray(nums=[2, 0, 2], queries=[[0, 2, 1], [0, 2, 1], [1, 1, 3]]))
print(a.minZeroArray(nums=[4, 3, 2, 1], queries=[[1, 3, 2], [0, 2, 1]]))
