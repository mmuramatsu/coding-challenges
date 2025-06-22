class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7

        # Base cases for a single row or column
        if m == 1:
            return (3 * 2 ** (n - 1)) % MOD
        if n == 1:
            return (3 * 2 ** (m - 1)) % MOD

        # Function to generate all valid colorings for a single column of height m
        def generate_valid_coloring(colors, height, current_coloring, all_colorings):
            if height <= 0:
                all_colorings.append(current_coloring.copy())
                return

            for color in colors:
                if not current_coloring or current_coloring[-1] != color:
                    current_coloring.append(color)
                    next_colors = [0, 1, 2]
                    generate_valid_coloring(
                        next_colors, height - 1, current_coloring, all_colorings
                    )
                    current_coloring.pop()

        def findCombination(height):
            result = []
            data = []
            generate_valid_coloring([0, 1, 2], height, data, result)
            return result

        # Generate all valid column colorings of height m
        valid_coloring = findCombination(m)
        v_lenght = len(valid_coloring)

        M = [[0] * v_lenght for _ in range(v_lenght)]

        # M[i][j] = 1 if valid coloring j can be placed to the right of valid coloring i
        for i in range(v_lenght):
            for j in range(v_lenght):
                is_compatible = True
                for k in range(m):
                    if valid_coloring[i][k] == valid_coloring[j][k]:
                        is_compatible = False
                        break
                if is_compatible:
                    M[i][j] = 1

        # Function to multiply two matrices
        def multiply(A, B):
            C = [[0] * v_lenght for _ in range(v_lenght)]
            for i in range(v_lenght):
                for j in range(v_lenght):
                    for l in range(v_lenght):
                        C[i][j] = (C[i][j] + A[i][l] * B[l][j]) % MOD
            return C

        # Function for matrix exponentiation
        def power(matrix, exp):
            result = [[0] * v_lenght for _ in range(v_lenght)]
            for i in range(v_lenght):
                result[i][i] = 1
            while exp > 0:
                if exp % 2 == 1:
                    result = multiply(result, matrix)
                matrix = multiply(matrix, matrix)
                exp //= 2
            return result

        # Calculate M^(n-1)
        Mn = power(M, n - 1)

        # Initial state: a vector of ones, as any valid column coloring can be the first column
        initial_state = [1] * v_lenght
        final_state = [0] * v_lenght

        # Multiply the initial state by the resulting matrix
        for j in range(v_lenght):
            for i in range(v_lenght):
                final_state[j] = (final_state[j] + initial_state[i] * Mn[i][j]) % MOD

        # The total number of valid colorings is the sum of the final state
        return sum(final_state) % MOD


a = Solution()
print(a.colorTheGrid(m=1, n=1))
print(a.colorTheGrid(m=1, n=2))
print(a.colorTheGrid(m=2, n=2))
print(a.colorTheGrid(m=1, n=50))
print(a.colorTheGrid(m=5, n=5))
