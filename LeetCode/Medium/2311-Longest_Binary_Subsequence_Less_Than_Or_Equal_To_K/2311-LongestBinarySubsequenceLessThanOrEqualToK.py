class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        """
        Given a binary string `s` and an integer `k`, our task is to find the
        longer subsequence that form a number less or equal to `k`.

        The idea is pretty simple, we're going to loop throught `s` from right
        to left (LSB to MSB) forming the respective decimal number using the 0s
        and 1s from `s`. As the number can have leading zeroes, we going to add
        every single zero that we find in `s` to the answer. When we face a "1",
        we need to check is we add this "1" the number will still be less than
        or equal to `k`.

        So the idea is, if `s[i] == "0"`, `length += 1`. Let `mult` be a
        variable that control in which binary place we need to add the digit, if
        `s[i] == "1"` and `mult + num <= k`, then we can add a new 1 to as this
        will form a number less than or equal to `k`, so we increase the
        `length`.
        """
        length = 0
        n = len(s)
        mult = 1
        num = 0

        for i in range(n - 1, -1, -1):
            if s[i] == "1":
                if mult + num <= k:
                    num = mult + num
                    mult <<= 1
                    length += 1
            else:
                length += 1
                mult <<= 1

        return length


a = Solution()
print(a.longestSubsequence(s="1001010", k=5))
print(a.longestSubsequence(s="00101001", k=1))
