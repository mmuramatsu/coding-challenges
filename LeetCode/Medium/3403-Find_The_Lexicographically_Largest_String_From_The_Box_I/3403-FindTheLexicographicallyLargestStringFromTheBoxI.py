class Solution:
    def answerString(self, word: str, k: int) -> str:
        """
        Given a string of lenght n and a number of friends k, our task is to
        find the largest lexicographically string after splitting the string
        into k parts.

        As we need to divide the string in k parts, so that there are no empty
        strings, the maximum length possible is "n - (k - 1)", let's call this
        M. So, the idea is to compare every single substring of lenght M,
        looking for the lexicographically largest. For each i in range [0, n-1],
        we slice our string to get a string of lenght M starting from i. We need
        to manage the edge case, where we can't have a string with length M
        starting in i, because is out of bounds. To solve this we just find the
        minimum between n and M.

        OBS 1: The operators `>` and `<` for string comparison in Python already
        perform lexicographical comparison, which is crucial here.

        OBS 2: In the case where two substrings are starting at the same i, but
        with different ends, the largest one (in size) will always be largest
        lexicographically string, because the shortest (in size) is a prefix of
        the largest (in size). That's why we don't need compare strings shorter
        than M, except at the end of the string. This optimization significantly
        reduces the number of string comparisons needed, as we don't need to
        check all possible lengths for each starting position i. You only need
        to check the longest one that fits the M constraint.
        """
        if k == 1:
            return word

        n = len(word)
        largest_word = ""

        for i in range(n):
            # cur_word = word[i : min(n, i + (n - (k - 1)))]
            cur_word = word[i : n if n < i + n - (k - 1) else i + n - (k - 1)]

            if cur_word > largest_word:
                largest_word = cur_word

        return largest_word


a = Solution()
print(a.answerString(word="dbca", k=2))
print(a.answerString(word="gggg", k=4))
print(a.answerString(word="dzca", k=2))
