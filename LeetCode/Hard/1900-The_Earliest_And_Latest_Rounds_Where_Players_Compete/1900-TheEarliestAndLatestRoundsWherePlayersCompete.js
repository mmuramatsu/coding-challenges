function create3DMatrixFunctional(dim1, dim2, dim3, initialValue = false) {
    return Array.from({ length: dim1 }, () =>
        Array.from({ length: dim2 }, () =>
            Array.from({ length: dim3 }, () => initialValue)
        )
    );
}

/**
 * @param {number} n
 * @param {number} firstPlayer
 * @param {number} secondPlayer
 * @return {number[]}
 */
var earliestAndLatest = function (n, firstPlayer, secondPlayer) {
    firstPlayer -= 1;
    secondPlayer -= 1;
    let memo = create3DMatrixFunctional(28, 28, 28);
    let min_round = Number.MAX_SAFE_INTEGER;
    let max_round = Number.MIN_SAFE_INTEGER;
    let alive = (1 << n) - 1;

    var solve = function (alive, p1, p2, l, r, round, l_count, m_count, r_count) {
        if (l >= r)
            solve(alive, p1, p2, 0, n - 1, round + 1, l_count, m_count, r_count);
        else if ((alive & (1 << l)) == 0)
            solve(alive, p1, p2, l + 1, r, round, l_count, m_count, r_count);
        else if ((alive & (1 << r)) == 0)
            solve(alive, p1, p2, l, r - 1, round, l_count, m_count, r_count);
        else if (l == p1 && r == p2) {
            min_round = Math.min(min_round, round);
            max_round = Math.max(max_round, round);
        }
        else if (!memo[l_count][m_count][r_count]) {
            memo[l_count][m_count][r_count] = true;

            if (l != p1 && l != p2) {
                solve(
                    alive ^ (1 << l),
                    p1,
                    p2,
                    l + 1,
                    r - 1,
                    round,
                    l_count - (l < p1),
                    m_count - (l > p1 && l < p2),
                    r_count - (l > p2));
            }

            if (r != p1 && r != p2) {
                solve(
                    alive ^ (1 << r),
                    p1,
                    p2,
                    l + 1,
                    r - 1,
                    round,
                    l_count - (r < p1),
                    m_count - (r > p1 && r < p2),
                    r_count - (r > p2));
            }
        }
    }

    solve(
        alive,
        firstPlayer,
        secondPlayer,
        0,
        n - 1,
        1,
        firstPlayer,
        secondPlayer - firstPlayer - 1,
        n - 1 - secondPlayer);

    return [min_round, max_round];
};