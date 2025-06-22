class Solution:
    # DP solution
    def getWordsInLongestSubsequence1(
        self, words: list[str], groups: list[int]
    ) -> list[str]:
        n = len(words)
        dp = [1] * n
        parent = [-1] * n

        def hamming_distance(str1, str2):
            lenght = len(str1)
            h = 0

            for i in range(lenght):
                if str1[i] != str2[i]:
                    h += 1

            return h

        for i in range(n):
            for j in range(0, i):
                if (
                    groups[i] != groups[j]
                    and len(words[i]) == len(words[j])
                    and hamming_distance(words[i], words[j]) == 1
                ):
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j

        aux = dp.index(max(dp))
        ans = []

        while aux != -1:
            ans.append(words[aux])
            aux = parent[aux]

        return ans[::-1]

    # DP solution optimized
    def getWordsInLongestSubsequence(
        self, words: list[str], groups: list[int]
    ) -> list[str]:
        n = len(words)
        dp = [1] * n
        parent = [-1] * n

        for i in range(n):
            for j in range(0, i):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]):
                    # Hamming distance.
                    h = 0
                    for k in range(len(words[j])):
                        if words[i][k] != words[j][k]:
                            h += 1

                        # Condition to stop early.
                        if h > 1:
                            break

                    if h == 1:
                        if dp[j] + 1 > dp[i]:
                            dp[i] = dp[j] + 1
                            parent[i] = j

        aux = dp.index(max(dp))
        ans = []

        while aux != -1:
            ans.append(words[aux])
            aux = parent[aux]

        return ans[::-1]


a = Solution()
print(a.getWordsInLongestSubsequence(words=["bab", "dab", "cab"], groups=[1, 2, 2]))
print(a.getWordsInLongestSubsequence(words=["a", "b", "c", "d"], groups=[1, 2, 3, 4]))
