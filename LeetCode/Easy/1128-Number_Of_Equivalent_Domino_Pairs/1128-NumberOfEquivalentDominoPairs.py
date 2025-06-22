from collections import defaultdict, Counter


class Solution:
    """
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        ans = 0

        while len(dominoes) > 1:
            i = 1
            matched = 1
            while i < len(dominoes):
                if dominoes[0] == dominoes[i] or (
                    dominoes[0][0] == dominoes[i][1]
                    and dominoes[0][1] == dominoes[i][0]
                ):
                    dominoes.pop(i)
                    matched += 1
                else:
                    i += 1

            dominoes.pop(0)
            ans += (matched * (matched - 1)) // 2

        return ans
    """

    """
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        ans = 0
        freq = defaultdict(int)

        for domino in dominoes:
            freq[tuple(sorted(domino))] += 1

        for _, v in freq.items():
            if v > 1:
                ans += (v * (v - 1)) // 2

        return ans
    """

    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        ans = 0
        freq = Counter(tuple(sorted(domino)) for domino in dominoes)

        for _, v in freq.items():
            if v > 1:
                ans += (v * (v - 1)) // 2

        return ans


a = Solution()
print(a.numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]))
print(a.numEquivDominoPairs([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]))
print(a.numEquivDominoPairs([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2], [2, 1]]))
