from collections import Counter, defaultdict


class Solution:
    # Checking equal and unequal sequences separately. Beats 46.21%
    def longestPalindrome1(self, words: list[str]) -> int:
        unequal = defaultdict(int)
        equal = defaultdict(int)

        for w in words:
            if w[0] == w[1]:
                equal[w] += 1
            else:
                unequal[w] += 1

        odd = True
        ans = 0

        for _, v in equal.items():
            if v & 1 and odd:
                ans += v
                odd = False
            else:
                ans += v - (1 if v & 1 else 0)

        already_seem = set()

        for k, v in unequal.items():
            if k not in already_seem:
                if k[::-1] in unequal:
                    ans += (v if v < unequal[k[::-1]] else unequal[k[::-1]]) << 1

                already_seem.add(k[::-1])
                already_seem.add(k)

        return ans << 1

    # Checking in the same loop. Beats 82.98%
    def longestPalindrome(self, words: list[str]) -> int:
        freq = Counter(words)

        centered = False
        ans = 0

        for k, v in freq.items():
            backwards = k[::-1]
            # For a key k form a palindrome sequence we need that the inverse of
            # k is in freq. For k[0]==k[1], this condition is true.
            if backwards in freq:
                # For the case k[0]==k[1], we can add n copies of k, as long as
                # n is even, and we will still have a palindrome. However, we
                # can have only one key with odd copies, which can be placed in
                # the center of the string and we will still have a palindrome.
                if k[0] == k[1]:
                    if v & 1:
                        ans += v - 1
                        centered = True
                    else:
                        ans += v
                else:
                    # Each key to form a palindrome needs to be paired with its
                    # inverse, so we need to choose min(freq[k], freq[k[::-1]])
                    ans += v if v < freq[backwards] else freq[backwards]

        if centered:
            ans += 1

        return ans << 1


a = Solution()
print(a.longestPalindrome(["lc", "cl", "gg"]))
print(a.longestPalindrome(["ab", "ty", "yt", "lc", "cl", "ab"]))
print(a.longestPalindrome(["cc", "ll", "xx"]))
print(
    a.longestPalindrome(
        [
            "dd",
            "aa",
            "bb",
            "dd",
            "aa",
            "dd",
            "bb",
            "dd",
            "aa",
            "cc",
            "bb",
            "cc",
            "dd",
            "cc",
        ]
    )
)
