from collections import deque


class Solution:
    # BFS solution. Beats 99.13%
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        """
        It's given to us, a NxN board. Each position of that board has a value.
        An empty position is represented by -1 and any number different of this
        is a ladder or a snake which will take us to the position equals to the
        value found in that space.

        Each cell is labeled from 1 to n^2. The start of the board is in the
        position (n-1, 0). The board is meant to be interpreted in Boustrophedon
        style, in which alternate lines are written  in reversed. For example,
        for n=3, we have:
        7 8 9
        6 5 4
        1 2 3

        Our task is to find the minimum steps to get to the n^2 position, if
        it's possible, otherwise, return -1. To make this, we can use BFS to
        find the shortest path to the end.

        First, we're going to convert the 2D board into a 1D array to make
        movement simpler. Our `boustrophedon_array` will have (n^2)+1 positions.
        Let `boustrophedon_array[i]` be the value of board founded in the
        position labeled as i.

        Starting from (n-1, 0), the idea is to convert two rows and repeat this
        until the x coordinate is positive. Using three while loops, the first
        one will check if x >= 0. The second one will convert a row from left to
        right. The third will convert a row from right to left. We need to
        control three variables `x` and `y`, which is the positions in the board
        and `i`, the position in the `boustrophedon_array`. OBS: The third loop
        will only run if x >= 0. This condition will be false if n is odd.

        From now on we will not use the board anymore.

        The `boustrophedon_array` can be interpreted as a graph in which each
        position `i` is a node that has the next 6 positions as neighbors. So,
        our BFS queue will store the tuples (i, step). The starting point is
        (1, 0) (position 1 at step 0). After we pop an element from our queue we
        check if this position is equal to n^2, if so, we return the step,
        otherwise, for each j in [1,6], we enqueue (pos+j, step+1). If in the
        position pos+j we have a ladder or a snake we need to enqueue the
        destination, so we're going to enqueue
        (`boustrophedon_arra[pos+j]`, step+1). We use a boolean array to avoid
        revisiting nodes.

        If we end our BFS without reaching n^2 position, we return -1.
        """
        n = len(board)
        n_squared = n**2
        boustrophedon_array = [0] * (n_squared + 1)

        y = 0
        x = n - 1
        i = 1

        # Converting 2D board matrix into a 1D boustrophedon_array
        while x >= 0:
            while y < n:
                boustrophedon_array[i] = board[x][y]
                y += 1
                i += 1

            x -= 1
            y -= 1

            if x >= 0:
                while y >= 0:
                    boustrophedon_array[i] = board[x][y]
                    y -= 1
                    i += 1

            x -= 1
            y += 1

        def bfs():
            queue = deque([(1, 0)])
            visited = [False] * (n_squared + 1)
            visited[1] = True

            while queue:
                pos, step = queue.popleft()

                if pos == n_squared:
                    return step

                for i in range(1, 7):
                    next_pos = pos + i
                    if next_pos <= n_squared:
                        if not visited[next_pos]:
                            visited[next_pos] = True
                            if boustrophedon_array[next_pos] == -1:
                                queue.append((next_pos, step + 1))
                            else:
                                queue.append((boustrophedon_array[next_pos], step + 1))

            # If we complete the bfs without reaching n_squared, return -1
            return -1

        return bfs()


a = Solution()
print(
    "ans: ",
    a.snakesAndLadders(
        board=[
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 35, -1, -1, 13, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 15, -1, -1, -1, -1],
        ]
    ),
)
print("ans: ", a.snakesAndLadders(board=[[-1, -1], [-1, 3]]))
print("ans: ", a.snakesAndLadders(board=[[1, 1, -1], [1, 1, 1], [-1, 1, 1]]))
