class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        k = 0

        for n in arr:
            if n & 1:
                k += 1
                if k == 3:
                    return True
            else:
                k = 0

        return False


a = Solution()
print(a.threeConsecutiveOdds(arr=[2, 6, 4, 1]))
print(a.threeConsecutiveOdds(arr=[1, 2, 34, 3, 4, 5, 7, 23, 12]))
