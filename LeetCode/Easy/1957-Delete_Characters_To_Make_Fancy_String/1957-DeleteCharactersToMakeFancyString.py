class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        prev = s[0]
        count = 1
        ans = [s[0]]

        for c in s[1:]:
            if prev == c:
                count += 1
            else:
                count = 1

            if count < 3:
                ans.append(c)

            prev = c

        return "".join(ans)


a = Solution()
print(a.makeFancyString(s="leeetcode"))
print(a.makeFancyString(s="aaabaaaa"))
print(a.makeFancyString(s="aab"))
