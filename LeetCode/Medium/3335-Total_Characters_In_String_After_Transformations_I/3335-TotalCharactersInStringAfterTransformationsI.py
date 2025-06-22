from collections import Counter


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7

        # dp array to store the length of the transformed string after a certain number of steps
        # dp[i] = length after i effective transformations
        dp = [0] * (t + 26)

        # Base case: After 0 transformations, the length of any single character is 1
        for i in range(26):
            dp[i] = 1

        # Calculate the lengths for subsequent transformations
        for i in range(26, t + 26):
            # The length at step i is the sum of lengths 26 steps ago and 25 steps ago
            # This captures the cyclic nature of the alphabet and the 'z' -> 'ab' expansion
            dp[i] = (dp[i - 26] + dp[i - 25]) % MOD

        # Count the frequency of each character in the input string
        freq = Counter(s)

        # Calculate the total length of the transformed string
        ans = 0
        for char, count in freq.items():
            # For each character, find its position in the alphabet (0 for 'a', 1 for 'b', etc.)
            char_index = ord(char) - ord("a")

            # The length of the transformed character after t steps is given by dp[char_index + t]
            # Multiply by the frequency of the character and add to the total length
            ans = (ans + dp[char_index + t] * count) % MOD

        return ans


a = Solution()
print(a.lengthAfterTransformations(s="abcyy", t=2))
print(a.lengthAfterTransformations(s="abcyy", t=30))
print(a.lengthAfterTransformations(s="azbk", t=1))
# print(a.lengthAfterTransformations(s="jqktcurgdvlibczdsvnsg", t=7517))
