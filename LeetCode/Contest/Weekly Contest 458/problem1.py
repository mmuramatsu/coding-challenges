class Solution:
    def processStr(self, s: str) -> str:
        n = len(s)
        ans = []

        for c in s:
            if c == "*":
                if len(ans) != 0:
                    ans.pop()
            elif c == "#":
                ans = ans + ans
            elif c == "%":
                ans.reverse()
            else:
                ans.append(c)

        return "".join(ans)


a = Solution()
print(a.processStr(s="a#b%*"))
print(a.processStr(s=""))
