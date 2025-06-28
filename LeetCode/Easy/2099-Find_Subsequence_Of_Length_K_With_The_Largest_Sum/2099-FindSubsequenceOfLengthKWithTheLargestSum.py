class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        idx = [(num, i) for i, num in enumerate(nums)]

        greatest = sorted(
            idx,
            reverse=True,
            key=lambda x: x[0],
        )[:k]

        idx_greatest = sorted(greatest, key=lambda x: x[1])

        ans = [num for num, _ in idx_greatest]

        return ans

    def maxSubsequence1(self, nums: list[int], k: int) -> list[int]:
        aux = nums.copy()
        aux.sort(reverse=True)
        aux = aux[:k]

        n = len(nums)

        picked = [False] * n

        ans = []

        for _ in range(k):
            i = 0
            while i < n:
                if nums[i] in aux and not picked[i]:
                    break
                i += 1

            aux.remove(nums[i])
            picked[i] = True
            ans.append(nums[i])

        return ans


a = Solution()
print(a.maxSubsequence(nums=[2, 1, 3, 3], k=2))
print(a.maxSubsequence(nums=[-1, -2, 3, 4], k=3))
print(a.maxSubsequence(nums=[3, 4, 3, 3], k=2))
print(a.maxSubsequence(nums=[1, 3, 4, 5, 2], k=2))
