class Solution:
    # Matrix exponentiation
    def fib(self, n: int) -> int:
        def matrix_mult(A, B):
            n = len(A)
            result = [[0] * n for _ in range(n)]

            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        result[i][j] += A[k][j] * B[i][k]

            return result

        def matrix_exp(M, n):
            if n == 1:
                return M

            result = [[1, 0], [0, 1]]

            while n > 0:
                if n & 1:
                    result = matrix_mult(result, M)
                M = matrix_mult(M, M)

                n //= 2

            return result

        if n == 0:
            return 0

        if n == 1:
            return 1

        M = [[1, 1], [1, 0]]

        M = matrix_exp(M, n - 1)

        first_state = [1, 0]

        """
        last_state = [
            M[0][0] * first_state[0] + M[0][1] * first_state[1],
            M[1][0] * first_state[0] + M[1][1] * first_state[1],
        ]
        """

        return M[0][0] * first_state[0] + M[0][1] * first_state[1]

    # DP + Botton-up
    def DP_fibonacci(n):
        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1

        tabulation = [0] * (n + 1)
        tabulation[0] = 0
        tabulation[1] = 1
        tabulation[2] = 1

        for i in range(3, n + 1):
            tabulation[i] = tabulation[i - 1] + tabulation[i - 2]

        return tabulation[n]

    # DP + Botton-up space optimized
    def DP_fibonacci1(n):
        if n <= 1:
            return n

        prev = 0
        curr = 1

        for _ in range(2, n + 1):
            prev, curr = curr, curr + prev

        return curr

    # DP + Top-down
    def DP_fibonacci2(n):
        memo = {0: 0, 1: 1}

        def fibo(n):
            if n in memo:
                return memo[n]

            return fibo(n - 1) + fibo(n - 2)

        return fibo(n)

    # Math formula
    def math_fibonacci(n):
        sqrt5 = 5**0.5
        fibN = ((1 + sqrt5) / 2) ** n - ((1 - sqrt5) / 2) ** n
        return round(fibN / sqrt5)
