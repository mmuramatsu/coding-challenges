class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = 1
        prev = word[0]

        for i in range(1, len(word)):
            if word[i] == prev:
                count += 1

            prev = word[i]

        return count


a = Solution()
print(a.possibleStringCount(word="abbcccc"))
print(a.possibleStringCount(word="abcd"))
print(a.possibleStringCount(word="aaaa"))
