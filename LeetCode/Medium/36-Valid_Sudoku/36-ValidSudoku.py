from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        lines = [defaultdict(int) for _ in range(9)]
        columns = [defaultdict(int) for _ in range(9)]
        squares = [defaultdict(int) for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    lines[i][board[i][j]] += 1
                    columns[j][board[i][j]] += 1

                    # Determine which 3x3 square the current element belongs to
                    square_row_index = i // 3
                    square_col_index = j // 3
                    square_index = square_row_index * 3 + square_col_index

                    squares[square_index][board[i][j]] += 1

        for i in range(9):
            for digit in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                if lines[i][digit] > 1:
                    return False
                if columns[i][digit] > 1:
                    return False
                if squares[i][digit] > 1:
                    return False

        return True


a = Solution()
print(
    a.isValidSudoku(
        board=[
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
print(
    a.isValidSudoku(
        board=[
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
