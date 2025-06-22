class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"

        if n == 1:
            return ans

        last_letter = ""

        for _ in range(n - 1):
            aux = ""
            count = 1
            last_letter = ans[0]

            for i in range(1, len(ans)):
                if last_letter == ans[i]:
                    count += 1
                else:
                    aux += str(count) + last_letter

                    count = 1
                    last_letter = ans[i]

            aux += str(count) + last_letter
            ans = aux

        return ans


a = Solution()
print(a.countAndSay(1))
print(a.countAndSay(2))
print(a.countAndSay(3))
print(a.countAndSay(4))
print(a.countAndSay(5))
print(a.countAndSay(6))
