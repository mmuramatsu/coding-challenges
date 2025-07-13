class Solution:
    def earliestAndLatest(
        self, n: int, firstPlayer: int, secondPlayer: int
    ) -> list[int]:
        firstPlayer -= 1
        secondPlayer -= 1
        min_round = float("inf")
        max_round = float("-inf")
        alive_mask = (1 << n) - 1
        memo = [[[False] * 28 for _ in range(28)] for _ in range(28)]

        def solve(alive, l, r, round, left_count, mid_count, right_count):
            if l >= r:
                # Next rount
                solve(alive, 0, n - 1, round + 1, left_count, mid_count, right_count)
            elif alive & (1 << l) == 0:
                # If `l` is not alive
                solve(alive, l + 1, r, round, left_count, mid_count, right_count)
            elif alive & (1 << r) == 0:
                # If `r` is not alive
                solve(alive, l, r - 1, round, left_count, mid_count, right_count)
            elif l == firstPlayer and r == secondPlayer:
                # If we found the match P1 vs P2
                # Update the max and min
                nonlocal min_round, max_round
                min_round = min(min_round, round)
                max_round = max(max_round, round)
            elif not memo[left_count][mid_count][right_count]:
                # If not calculated yet

                # Mark as calculated
                memo[left_count][mid_count][right_count] = True

                # Let r wins
                if l != firstPlayer and l != secondPlayer:
                    solve(
                        alive ^ (1 << l),
                        l + 1,
                        r - 1,
                        round,
                        left_count - (l < firstPlayer),
                        mid_count - (l > firstPlayer and l < secondPlayer),
                        right_count - (l > secondPlayer),
                    )

                # Let l wins
                if r != firstPlayer and r != secondPlayer:
                    solve(
                        alive ^ (1 << r),
                        l + 1,
                        r - 1,
                        round,
                        left_count - (r < firstPlayer),
                        mid_count - (r > firstPlayer and r < secondPlayer),
                        right_count - (r > secondPlayer),
                    )

        solve(
            alive_mask,
            0,
            0,
            0,
            firstPlayer,
            n - 1 - secondPlayer,
            secondPlayer - firstPlayer - 1,
        )

        return [min_round, max_round]

    def earliestAndLatest1(
        self, n: int, firstPlayer: int, secondPlayer: int
    ) -> list[int]:
        firstPlayer -= 1
        secondPlayer -= 1
        min_round = float("inf")
        max_round = float("-inf")
        alive = [True] * n
        memo = [[[False] * 28 for _ in range(28)] for _ in range(28)]

        def solve(alive, l, r, round, left_count, mid_count, right_count):
            if l >= r:
                # Next rount
                solve(alive, 0, n - 1, round + 1, left_count, mid_count, right_count)
            elif not alive[l]:
                # If `l` is not alive
                solve(alive, l + 1, r, round, left_count, mid_count, right_count)
            elif not alive[r]:
                # If `r` is not alive
                solve(alive, l, r - 1, round, left_count, mid_count, right_count)
            elif l == firstPlayer and r == secondPlayer:
                # If we found the match P1 vs P2
                # Update the max and min
                nonlocal min_round, max_round
                min_round = min(min_round, round)
                max_round = max(max_round, round)
            elif not memo[left_count][mid_count][right_count]:
                # If not calculated yet

                # Mark as calculated
                memo[left_count][mid_count][right_count] = True

                copy = alive.copy()
                # Let r wins
                if l != firstPlayer and l != secondPlayer:
                    copy[l] = False
                    solve(
                        copy,
                        l + 1,
                        r - 1,
                        round,
                        left_count - (l < firstPlayer),
                        mid_count - (l > firstPlayer and l < secondPlayer),
                        right_count - (l > secondPlayer),
                    )
                    copy[l] = True

                # Let l wins
                if r != firstPlayer and r != secondPlayer:
                    copy[r] = False
                    solve(
                        copy,
                        l + 1,
                        r - 1,
                        round,
                        left_count - (r < firstPlayer),
                        mid_count - (r > firstPlayer and r < secondPlayer),
                        right_count - (r > secondPlayer),
                    )

        solve(
            alive,
            0,
            0,
            0,
            firstPlayer,
            n - 1 - secondPlayer,
            secondPlayer - firstPlayer - 1,
        )

        return [min_round, max_round]


a = Solution()
print(a.earliestAndLatest(n=11, firstPlayer=2, secondPlayer=4))
print(a.earliestAndLatest(n=5, firstPlayer=1, secondPlayer=5))
