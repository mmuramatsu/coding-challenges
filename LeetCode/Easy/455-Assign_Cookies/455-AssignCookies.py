class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        n = len(g)
        m = len(s)
        g.sort()
        s.sort()

        j = 0
        count = 0

        for i in range(n):
            while j < m and g[i] > s[j]:
                j += 1

            if j < m:
                count += 1
                j += 1
            else:
                break

        return count


a = Solution()
print(a.findContentChildren(g=[1, 2, 3], s=[1, 1]))
print(a.findContentChildren(g=[1, 2], s=[1, 2, 3]))
