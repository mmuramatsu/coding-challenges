class Solution:
    def totalNQueens(self, n: int) -> int:
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

        ans = 0

        def backtracking(x):
            if x == n:
                nonlocal ans
                ans += 1
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
print(a.totalNQueens(1))
print(a.totalNQueens(4))
print(a.totalNQueens(5))
