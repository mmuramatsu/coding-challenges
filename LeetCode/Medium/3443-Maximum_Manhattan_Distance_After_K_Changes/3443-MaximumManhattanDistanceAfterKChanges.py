class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        """
        Given a string `s` composed of only with the characters "N", "S", "E"
        and "W", representing the cardial directions North, South, East and
        West. It's also given a integer `k`. Our task is, starting from the
        position (0, 0), find the maximum Manhattan Distance
        (|xi - xj| + |yi - yj|) possible by changing at most `k` characters of
        `s`.

        There are two key points to solve this problem. The first one is that
        opposite directions lead us to a conflicts, and if we solve this
        conflict we can increase the Manhattan Distance by 2. For example if we
        have the string "NS...", the Manhattan Distance at `i = 1` is 0, because
        "N" will increase the y coordinate by 1 and "S" decrease the coordinate
        by 1. If we solve this conflict, for example, changing "S" by "N", the
        distance at `i = 1` will be 2 (first "N" give +1 and the -1 given by the
        "S" will become +1 too, therefore +2.).

        The second key point is that, if in the step `i`, we have a string that
        has no conflicts, then the maximum Manhattan Distance will be `i + 1`.
        For example, if we have "NENN...", at, step `i = 3`, the Manhattan
        Distance is 4 (+3 from "N" occurencies and +1 from "E".), which is equal
        to `i + 1`.

        So, we're going to create four variables to store the movement in each
        coordinate. For each character `c` at position `i`, we're going to add
        the movement to the respective variable, and calculate the conflicts we
        get so far, which is the sum of minimum the movement in y-axis plus
        x-axis. The idea here is that if we have 3 "N" and 2 "S", the number of
        conflicts coordinates are 2, the remaining "N" are not in confict.

        So, if the number of conflicts are less than or equal to `k`, we can
        solve ALL the conflicts, which will lead us to the maximum distance of
        `i + 1`. If the number of conflicts are greater than `k`, we can't solve
        every conflict but we can solve at most `k`, so the maximum disttance
        will be `(i + 1) - (conflicts * 2) + (k * 2)`.

        Why? First, as I said before, a conflicts solved will lead us to +2 in
        the maximum distance. In the same way, if we have no conflicts and we
        change a letter to one that has conflict, our maximum distance will
        reduce in 2. Let's analyse term by term. The term "(i + 1)", represents
        the maximum distance of a perfect string, with no conflicts,
        "-(conflicts * 2)", is the decrement caused by the conflicts that we
        have and "(k * 2)", is the increment after we solve at most `k`
        conflicts.

        The answer of this problem is the maximum that we can find in each step.
        """
        north = south = west = east = 0
        ans = 0

        for i, c in enumerate(s):
            if c == "N":
                north += 1
            elif c == "S":
                south += 1
            elif c == "E":
                east += 1
            else:
                west += 1

            conflicts = min(north, south) + min(east, west)

            max_dist = i + 1

            if k < conflicts:
                max_dist = max_dist - (conflicts * 2) + (k * 2)

            ans = max(ans, max_dist)

        return ans

    def maxDistance1(self, s: str, k: int) -> int:
        x = y = 0
        ans = 0

        for i, c in enumerate(s):
            if c == "N":
                y += 1
            elif c == "S":
                y -= 1
            elif c == "E":
                x += 1
            else:
                x -= 1

            print(f"max({ans}, min({(abs(x) + abs(y) + k * 2)}, {i + 1}))")

            ans = max(ans, min((abs(x) + abs(y) + k * 2), i + 1))

        return ans


a = Solution()
print(a.maxDistance(s="NWSE", k=1))
print(a.maxDistance(s="NSWWEW", k=3))
print(a.maxDistance(s="WEWE", k=1))
