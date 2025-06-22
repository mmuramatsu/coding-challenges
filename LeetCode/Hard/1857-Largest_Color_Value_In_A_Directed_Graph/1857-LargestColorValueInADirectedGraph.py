from collections import defaultdict, deque


class Solution:
    # DFS + DP approach. Beats 49.43%.
    def largestPathValue1(self, colors: str, edges: list[list[int]]) -> int:
        """
        We need to run through all the paths of the graph and find the most
        repeated color in a path.

        The idea is to use DFS to run through all nodes. There is two major
        things we need to keep tracking: 1. Cycle detection and 2. Counter of
        colors of the path.

        1. To detect cycle, we gonna use a set `path`, which will store the
        nodes of the current path. If a node lead us to a node that are already
        in `path`, then we have a cycle. After a node is processed (i.e. all the
        neighbors are called and returned), we remove this node from `path`.

        2. The idea is to run DFS through all nodes, from 0 to n
        (len(colors)-1). Suppose we have this path:

        x_3 -> x_0 -> x_1 -> x_2

        First we gonna call `dfs(0)`, which will return the most repeated color
        in the path "x_0 -> x_1 -> x_2". Then we gonna try to call
        `dfs(1)` and `dfs(2)`, which are already processed (already
        in `visited` set), so we do nothing. Finally, we call `dfs(3)`, which
        will call `dfs(0)`, that we already calculated.

        So we gonna use DP to store the result for each node. We also know that
        the colors are letter from a-z, so, 26 possible colors. Let `dp[i][c]`
        be the maximum count of color c on any path starting from node i. The
        matrix `dp` size is Nx26, so, for each node we store the number of each
        colors find in that path.

        For each neighbor processed, we update the colors of the current node by
        doing `dp[current_node][c] = max(dp[current_node][c], dp[neighbor][c])`
        for each c in [0,25]. When all neighbors are processed, we give the
        current color count an increment.
        """
        graph = defaultdict(set)

        # Creating an adjacency list
        for u, v in edges:
            graph[u].add(v)

        def dfs(cur_node):
            # If it has cycle
            if cur_node in path:
                return float("inf")

            # Already processed (skip)
            if cur_node in visited:
                return 0

            visited.add(cur_node)
            path.add(cur_node)

            for neighbor in graph[cur_node]:
                if dfs(neighbor) == float("inf"):
                    return float("inf")

                # Update DP table
                for c in range(26):
                    # max(dp[cur_node][c], dp[neighbor][c])
                    dp[cur_node][c] = (
                        dp[cur_node][c]
                        if dp[cur_node][c] > dp[neighbor][c]
                        else dp[neighbor][c]
                    )

            # Remove from path
            path.remove(cur_node)

            # Add the current color
            dp[cur_node][ord(colors[cur_node]) - ord("a")] += 1

            return max(dp[cur_node])

        n = len(colors)
        visited = set()
        path = set()
        dp = [[0] * 26 for _ in range(n)]
        ans = 0

        for n in range(n):
            aux = dfs(n)

            if aux > ans:
                ans = aux

        return ans if ans != float("inf") else -1

    # BFS + DP approach. Beats 89.38%.
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        """
        We need to run through all the paths of the graph and find the most
        repeated color in a path.

        The idea is to use BFS to run through all nodes. To select which node
        we're going to visit, we gonna use topological sort-like strategy. The
        nodes will be selected when their in-degree (the number of incoming
        edges) is 0, which means that there's no other node before that one to
        be processed.

        First, we create the adjacency list and the `in_degree` array, where
        `in_degree[i]` is the number of incoming edges of node i. Then, we
        initialize a queue with the nodes that have in-degree == 0.

        Then we start our BFS. We pop a node u from the queue and increase the
        visited count of nodes. We update the color count of node u by doing
        `dp[cur_node][color_index] += 1` and update the `ans` which is the
        largest color value. Next step is to update our dp table. So, for each
        neighbor of u we update the neighbor cell of dp table by doing
        `dp[neighbor][c] = max(dp[cur_node][c], dp[neighbor][c])` for each c in
        [0,25]. We are taking the maximum because we want to carry forward the
        largest counts of each color encountered so far along any path leading
        to the current node. Then, we decrement by one the in-degree of the
        neighbor node, which can be interpreted as "we already processed one
        'dependency' of this node".

        Finally, if the in-degree of the neighbor node is equal to 0, we add
        this to the queue. It's important to note if we have a cycle in the
        graph, the node that start the cycle never get the in-degree to 0, which
        means that it never gets enqueued. So, if the count of visited nodes are
        less than n, we gonna return -1, due to a cycle.
        """
        graph = defaultdict(list)

        n = len(colors)
        in_degree = [0] * n
        dp = [[0] * 26 for _ in range(n)]

        # Creating an adjacency list
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1

        queue = deque([i for i in range(n) if in_degree[i] == 0])
        ans = 0
        visited = 0

        # BFS
        while queue:
            cur_node = queue.popleft()
            visited += 1

            color_index = ord(colors[cur_node]) - ord("a")
            dp[cur_node][color_index] += 1

            # max(ans, dp[cur_node][color_index])
            ans = ans if ans > dp[cur_node][color_index] else dp[cur_node][color_index]

            for neighbor in graph[cur_node]:
                # Update DP table
                for c in range(26):
                    dp[neighbor][c] = (
                        dp[cur_node][c]
                        if dp[cur_node][c] > dp[neighbor][c]
                        else dp[neighbor][c]
                    )
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if visited < n:
            return -1

        return ans


a = Solution()
print(a.largestPathValue(colors="abaca", edges=[[0, 1], [0, 2], [2, 3], [3, 4]]))
print(a.largestPathValue(colors="a", edges=[[0, 0]]))
