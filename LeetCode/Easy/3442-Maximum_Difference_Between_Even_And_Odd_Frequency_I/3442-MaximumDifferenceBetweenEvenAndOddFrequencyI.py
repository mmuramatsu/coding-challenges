from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        """
        This problem ask us to find the maximum of the `diff = a_1 - a_2`, where
        `a_1` is the frequency of some character in `s` that has odd
        repetitions, and `a_2` is the frequency of some character in `s` that
        has even repetitions.

        Our task is to maximize this difference, which means we need to find the
        maximum among the odd frequencies for a_1 and the minimum among the even
        frequencies for a_2.

        We can use a `Counter` object to make the count of each characters and
        initialize `a_1` with 0 and `a_2` with infinity. For each frequency `v`
        that we find if it's odd, we do `a_1 = max(a_1, v)`. If it's even, we do
        `min(a_2, v)`. Finally we return the `diff` value.
        """
        freq = Counter(s)

        a_1 = 0
        a_2 = float("inf")

        for _, v in freq.items():
            if v & 1:
                a_1 = a_1 if a_1 > v else v
            else:
                a_2 = a_2 if a_2 < v else v

        return a_1 - a_2


a = Solution()
print(a.maxDifference(s="aaaaabbc"))
print(a.maxDifference(s="abcabcab"))
