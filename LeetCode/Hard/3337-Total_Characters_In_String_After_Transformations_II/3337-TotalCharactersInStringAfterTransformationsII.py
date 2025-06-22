class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = 26  # Size of the alphabet

        # 1. Build the Transformation Matrix M
        # M[i][j] = 1 if the j-th character is in the transformation of the i-th character, else 0
        M = [[0] * n for _ in range(n)]
        for i in range(n):
            length = nums[i]
            start = (i + 1) % n  # The transformation starts with the next character
            for k in range(length):
                index = (start + k) % n
                M[i][index] = 1

        # Function to multiply two n x n matrices
        def multiply(A, B):
            C = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for l in range(n):
                        C[i][j] = (C[i][j] + A[i][l] * B[l][j]) % MOD
            return C

        # Function to compute matrix raised to the power of 'exp' using binary exponentiation
        # x^n = x^(2k) = (x^k)^2 if it's even.
        # x^n = x^(2k+1) = x * x^(2k) = x * (x^k)^2 if it's odd.
        def power(matrix, exp):
            result = [[0] * n for _ in range(n)]
            for i in range(n):
                result[i][i] = 1  # Initialize result as the identity matrix (M^0)
            while exp > 0:
                if exp % 2 == 1:
                    result = multiply(result, matrix)
                matrix = multiply(matrix, matrix)
                exp //= 2
            return result

        # 2. Compute M^t using binary exponentiation
        Mt = power(M, t)

        # 3. Create the initial frequency vector of characters in s
        initial_freq = [0] * n
        for char in s:
            initial_freq[ord(char) - ord("a")] += 1

        # 4. Compute the final frequency vector after t transformations
        # final_freq[j] = sum over all i (initial_freq[i] * Mt[i][j])
        final_freq = [0] * n
        for j in range(n):
            for i in range(n):
                final_freq[j] = (final_freq[j] + initial_freq[i] * Mt[i][j]) % MOD

        # 5. The total length is the sum of the frequencies of all characters
        return sum(final_freq) % MOD


a = Solution()
print(
    a.lengthAfterTransformations(
        s="abcyy",
        t=2,
        nums=[
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            2,
        ],
    )
)  # 7
print(
    a.lengthAfterTransformations(
        s="azbk",
        t=1,
        nums=[
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
        ],
    )
)  # 8
