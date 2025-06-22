class Solution:
    def maxRepeating1(self, sequence: str, word: str) -> int:
        n = len(sequence)
        m = len(word)

        dp = [0] * n

        for i in range(m - 1, n):
            if sequence[i - m + 1 : i + 1] == word:
                dp[i] = dp[i - m] + 1
            else:
                dp[i] = 0

        return max(dp)

    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        repeated = word
        while repeated in sequence:
            print(repeated)
            k += 1
            repeated += word
        return k


a = Solution()
print(a.maxRepeating(sequence="ababc", word="ab"))
print(a.maxRepeating(sequence="ababc", word="ba"))
print(a.maxRepeating(sequence="ababc", word="ac"))
print(a.maxRepeating(sequence="ababab", word="ab"))
print(a.maxRepeating(sequence="aaabaaaabaaabaaaabaaaabaaaabaaaaba", word="aaaba"))  # 6
