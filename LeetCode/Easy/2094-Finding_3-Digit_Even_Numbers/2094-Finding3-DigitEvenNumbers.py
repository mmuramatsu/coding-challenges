from collections import Counter


class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        ans = []
        freq = Counter(digits)

        for i in range(100, 999, 2):
            cur = Counter(str(i))

            flag = True
            for k, v in cur.items():
                if freq[int(k)] < v:
                    flag = False
                    break

            if flag:
                ans.append(i)

        return ans


a = Solution()
print(a.findEvenNumbers([2, 1, 3, 0]))
print(a.findEvenNumbers([2, 2, 8, 8, 2]))
print(a.findEvenNumbers([3, 7, 5]))
