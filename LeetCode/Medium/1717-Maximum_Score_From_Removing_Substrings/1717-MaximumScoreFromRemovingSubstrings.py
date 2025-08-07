class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove(s, sub):
            stack = []

            for c in s:
                if c == sub[1] and stack and stack[-1] == sub[0]:
                    stack.pop()
                else:
                    stack.append(c)

            return "".join(stack)

        ans = 0
        if y > x:
            first = "ba"
            second = "ab"
        else:
            first = "ab"
            second = "ba"

        new_s = remove(s, first)
        ans += ((len(s) - len(new_s)) // 2) * max(x, y)
        ans += ((len(new_s) - len(remove(new_s, second))) // 2) * min(x, y)

        return ans


a = Solution()
print(a.maximumGain(s="cdbcbbaaabab", x=4, y=5))
print(a.maximumGain(s="aabbaaxybbaabb", x=5, y=4))
