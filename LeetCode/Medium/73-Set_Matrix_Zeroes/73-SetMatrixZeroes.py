class Solution:
    # Let K be the number of zeros in matrix. The Space complexity is O(K).
    def setZeroes1(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_index = []
        rows = []
        columns = []

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_index.append((i, j))

        for r, c in zero_index:
            if r not in rows:
                matrix[r] = [0] * n
                rows.append(r)
            if c not in columns:
                for i in range(m):
                    matrix[i][c] = 0

                columns.append(c)

    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        zero_flag = False

        for i in range(m):
            if matrix[i][0] == 0:
                zero_flag = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

            if zero_flag:
                matrix[i][0] = 0


a = Solution()
print(a.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(a.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
