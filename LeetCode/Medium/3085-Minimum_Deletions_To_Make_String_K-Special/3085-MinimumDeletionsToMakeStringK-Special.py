from collections import Counter


class Solution:
    # Greedy solution. Beats 99.30%.
    def minimumDeletions(self, word: str, k: int) -> int:
        """
        Given a string `word` and an integer `k`, our task is to find the
        minimum number of occurencies of each character that needs to be deleted
        to form a k-special string, which is defined as a strign where,
        `|freq(word[i]) - freq(word[j])| <= k` for all indices i and j in the
        string.

        The idea to solve this problem is to choose a frequency of one character
        to be the minimum frequency possible and then compare to all other if
        they fit in the possible interval and how many deletions are need to
        form a k-special string with that minimum. We know that if `x` is the
        considered the minimum frequency of the string, then the maximum
        possible to form a k-special string will be  `x + k`. In this situation,
        there are 3 cases possible, let `y` be the frequency of a character `c`
        from `word`, so we have:
            - `x > y`: in this case `y` is below the minimum, which means that
            we need to delete all occurences of `c` to form a k-speacial string.
            So, `deletions += y`;
            - `y > x + k`: in this case, `y` is above the maximum, so we need to
            remove occurrences of `c` until it is within the maximum limit. So,
            `deletions += y - (x + k)`;
            - `x <= y <= (x + k)`: in this case, `y` is in the right interval,
            so we don't need to delete.

        We're going to repeat this considering all frenquencies as the minimum
        at each step and save the minimum founded, which will be our answer.
        This works because the string `word` is composed only by lowercase
        English letters, so we have at most 26 frequencies, given us a time
        complexity of O(n + C^2), where C=26 in this case.
            - `n` for count the frequencies and `C^2` to get the minimum number
            of deletions.

        The space complexity is dictated by the frequency map, which is O(C) in
        the worst case.
        """
        freq = Counter(word)
        ans = float("inf")

        for x in freq.values():
            deletions = 0

            for y in freq.values():
                if x > y:
                    deletions += y
                elif y > x + k:
                    deletions += y - (x + k)

            ans = min(ans, deletions)

        return ans


a = Solution()
print(a.minimumDeletions(word="aabcaba", k=0))
print(a.minimumDeletions(word="dabdcbdcdcd", k=2))
print(a.minimumDeletions(word="aaabaaa", k=2))
