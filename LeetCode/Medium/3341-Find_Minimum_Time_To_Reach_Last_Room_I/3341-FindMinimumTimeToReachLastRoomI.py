import heapq


class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])

        # Matrix that will store the minimum path for each node
        min_time = [[float("inf")] * m for _ in range(n)]
        min_time[0][0] = 0

        # Possible neighbors
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Heap queue, (time arrived to this node, x, y)
        queue = [(0, 0, 0)]

        while queue:
            time, i, j = heapq.heappop(queue)

            # If time (time arrived) is greater than min[i][j], it means that we already found a way to this node in a short time.
            # Works like a visited set, preventing us to revisit a node.
            if time > min_time[i][j]:
                continue

            # We reach the destination, so we return the time
            if i == n - 1 and j == m - 1:
                return time

            for dx, dy in neighbors:
                # Neightbor coordinates.
                n_x, n_y = i + dx, j + dy

                # Check if it is inside the borders.
                if 0 <= n_x < n and 0 <= n_y < m:
                    # Arrival time to get to node (n_x, n_y) is 1 (to move) + max(time, moveTime[n_x][n_y]).
                    # We can move only after the time moveTime[n_x][n_y], but if time is greater than moveTime[n_x][n_y], we are allowed to move.
                    arrival_time = 1 + (
                        time if time > moveTime[n_x][n_y] else moveTime[n_x][n_y]
                    )

                    # If the arrival time at node (n_x, n_y) is less than the minimum founded on min_time, we update and this neighbor to our heap to be processed.
                    if arrival_time < min_time[n_x][n_y]:
                        min_time[n_x][n_y] = arrival_time
                        heapq.heappush(queue, (arrival_time, n_x, n_y))

        return -1


a = Solution()
print(a.minTimeToReach([[0, 4], [4, 4]]))
print(a.minTimeToReach([[0, 0, 0], [0, 0, 0]]))
print(a.minTimeToReach([[0, 1], [1, 2]]))
print(a.minTimeToReach([[56, 93], [3, 38]]))  # 39
print(a.minTimeToReach([[94, 79, 62, 27, 69, 84], [6, 32, 11, 82, 42, 30]]))  # 72
