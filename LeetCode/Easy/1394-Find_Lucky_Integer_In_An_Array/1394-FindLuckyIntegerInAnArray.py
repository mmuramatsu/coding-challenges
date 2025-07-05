from collections import Counter


class Solution:
    def findLucky(self, arr: list[int]) -> int:
        freq = Counter(arr)

        ans = -1

        for k, v in freq.items():
            if k == v and k > ans:
                ans = k

        return ans


a = Solution()
print(a.findLucky(arr=[2, 2, 3, 4]))
print(a.findLucky(arr=[1, 2, 2, 3, 3, 3]))
print(a.findLucky(arr=[2, 2, 2, 3, 3]))
