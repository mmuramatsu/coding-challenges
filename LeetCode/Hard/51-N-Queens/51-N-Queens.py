class Solution:
    # Recurstion based approach. Beats 33.95%.
    def solveNQueens1(self, n: int) -> list[list[str]]:
        """
        The idea is to try to place a queen in every single column of the board,
        if it's possible, then we try the same in the next row. If we get to the row limit
        we append this solution if it's valid. Then we backtrack to the last branch,
        pop the last placed queen from the `placed` list and keep try to place a queen
        in other column to make sure that we try every single possibilities.

        The `is_safe` function, checks if this row, column or diagonal is free
        to place a queen. To check if two elements are in the same diagonal the
        difference between x0 and x1 and y0 and y1 need to be equal
        (`abs(x0 - x1) == abs(y0 - y1)`).
        """

        def is_safe(x, y, placed):
            for i, j in placed:
                if x == i or y == j:
                    return False

                if abs(x - i) == abs(y - j):
                    return False

            return True

        def place_queens(x, placed):
            if x == n:
                if len(placed) == n:
                    queens_position.append(placed.copy())
                return

            for i in range(n):
                if is_safe(x, i, placed):
                    placed.append((x, i))
                    place_queens(x + 1, placed)
                    placed.pop(-1)

        queens_position = []

        place_queens(0, [])

        ans = []

        for i in range(len(queens_position)):
            board = ["." * n for _ in range(n)]
            for x, y in queens_position[i]:
                board[x] = board[x][:y] + "Q" + board[x][y + 1 :]

            ans.append(board)

        return ans

    # Optimized backtracking version using sets to keep traking the occupied positions. Beats 79.66%
    def solveNQueens(self, n: int) -> list[list[str]]:
        """
        The idea is to try to place a queen in every single column of the board,
        if it's possible, then we try the same in the next row. If we get to the row limit
        we append this solution (We never gonna reach row == n without placing N queens,
        because the only way to go to the next row is by placing a queen in the current
        row). Then we backtrack to the last branch, pop the last placed queen
        and keep try to place a queen in other column to make sure that we try
        every single possibilities.

        As we place only one queen per row, we don't need have a set for row,
        the recursion does this for us. The `pos_diag_used` store the sums of
        `row + col` for placed queens. If two queens are on the same positive
        diagonal, their `row + col` will be the same. The `neg_diag_used` store
        the differences of `row - col` for placed queens. If two queens are on
        the same negative diagonal, their `row - col` will be the same.
        """
        column_used = set()
        pos_diag_used = set()
        neg_diag_used = set()
        queens = [0] * n

        ans = []

        def backtracking(x):
            if x == n:
                board = ["." * n for _ in range(n)]
                for r, c in enumerate(queens):
                    board[r] = board[r][:c] + "Q" + board[r][c + 1 :]

                ans.append(board)
                return

            for y in range(n):
                if not (
                    y in column_used or x + y in pos_diag_used or x - y in neg_diag_used
                ):
                    column_used.add(y)
                    pos_diag_used.add(x + y)
                    neg_diag_used.add(x - y)
                    queens[x] = y

                    backtracking(x + 1)

                    column_used.remove(y)
                    pos_diag_used.remove(x + y)
                    neg_diag_used.remove(x - y)

        backtracking(0)
        return ans


a = Solution()
assert a.solveNQueens(1) == [["Q"]]
assert a.solveNQueens(4) == [
    [".Q..", "...Q", "Q...", "..Q."],
    ["..Q.", "Q...", "...Q", ".Q.."],
]
assert a.solveNQueens(5) == [
    ["Q....", "..Q..", "....Q", ".Q...", "...Q."],
    ["Q....", "...Q.", ".Q...", "....Q", "..Q.."],
    [".Q...", "...Q.", "Q....", "..Q..", "....Q"],
    [".Q...", "....Q", "..Q..", "Q....", "...Q."],
    ["..Q..", "Q....", "...Q.", ".Q...", "....Q"],
    ["..Q..", "....Q", ".Q...", "...Q.", "Q...."],
    ["...Q.", "Q....", "..Q..", "....Q", ".Q..."],
    ["...Q.", ".Q...", "....Q", "..Q..", "Q...."],
    ["....Q", ".Q...", "...Q.", "Q....", "..Q.."],
    ["....Q", "..Q..", "Q....", "...Q.", ".Q..."],
]
