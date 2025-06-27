from collections import Counter, deque


class Solution:
    # BFS + Enumaration solution. Beats 53.66%
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        """
        Given a string `s` and an integer `k`, our task is to find the largest
        lexicographically subsequence of `s` that repeat `k` times.

        To solve this problem we're going to use a BFS + Enumaration approach.
        The idea is to try to form every single subsequence possible in
        lexicographically order. So, we start with a empty string and try to
        append "a", if the strign "a" is a subsequence of `s` that repeat `k`
        times, then it's a valid one, so we push this into our queue. Next,
        we're going to try append "b" to our empty string, and check if it's
        valid. We're going to do this for every single character.

        Then we pop an element from our queue, suppose it's "a", so, our current
        subsequence is "a" and again we're going to try to append characters
        from "a" to "z", looking for a valid subsequence that repteat `k` times.
        The last subsequence processed will be the largest lexicographically
        subsequence that repeat `k` tiems in `s`.

        A key point to optimize this solution is that the only characters of `s`
        that can form a valid subsequence that repeat `k` times is the
        characters that repeat more than `k` times in `s`. So, instead of trying
        every single character from "a" to "z", we can try only the possible
        characters.

        To verify if a subsequence is valid, we can use a two pointer approach.
        The idea is to make a pointer mark the current character of `s` and the
        other mark character of the subsequence, let's say `i` and `j`,
        respectively. If `s[i] == subseq[j]`, then we find a character that
        match, so we increment both, `i` and `j`, otherwise we increment only
        `i`. If `j` reach the `len(subseq)`, then we find one repetition of
        `subseq` in `s`, so we should reset `j` and decrement `k`. When
        `k == 0`, we find all `k` repetitions of `subseq` in `s`.

        OBS: A most optimize way to verify if `subseq` is a valid subsequence is
        by using this command:
            `it = iter(s); return all(ch in it for ch in subseq * k)`

        The idea is the same but using iterators. We can interpret this as "For
        every character `ch` in the string formed by repeating `subseq` `k`
        times, check if that `ch` can be found in `s` starting from the current
        position of the iterator `it`. If all characters from `subseq * k` are
        successfully found in `s` in their correct order, then the condition
        evaluates to True; otherwise, it's False."
        """
        freq = Counter(s)
        n = len(s)

        possible_chars = sorted([key for key, value in freq.items() if value >= k])

        queue = deque(possible_chars)

        def is_subsequence1(s, subseq, k):
            i = 0
            j = 0
            m = len(subseq)

            while i < n:
                if s[i] == subseq[j]:
                    j += 1
                    if j == m:
                        k -= 1
                        j = 0

                        if k == 0:
                            return True
                i += 1

            return False

        def is_subsequence(s, subseq, k):
            # Optimized
            it = iter(s)
            return all(ch in it for ch in subseq * k)

        ans = ""

        while queue:
            curr_subseq = queue.popleft()
            ans = curr_subseq

            for c in possible_chars:
                candidate = "".join([curr_subseq, c])
                if is_subsequence(s, candidate, k):
                    queue.append(candidate)

        return ans


a = Solution()
print(a.longestSubsequenceRepeatedK(s="letsleetcode", k=2))
print(a.longestSubsequenceRepeatedK(s="bb", k=2))
print(a.longestSubsequenceRepeatedK(s="ab", k=2))
print(a.longestSubsequenceRepeatedK(s="bbabbabbbbabaababab", k=3))
