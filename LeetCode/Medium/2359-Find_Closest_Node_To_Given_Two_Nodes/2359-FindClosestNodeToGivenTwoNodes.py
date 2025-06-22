from collections import defaultdict, deque


class Solution:
    # DFS solution. Beats 5.43%.
    def closestMeetingNode1(self, edges: list[int], node1: int, node2: int) -> int:
        """
        It's given to us an array of edges and two nodes. Our task is to find a
        node that are reachable by both nodes (node1 and node2) and the maximum
        between the distance from node1 to that node, and from node2 to that
        node is minimized
        "(min(max(dist1[0], dist2[0]), max(dist1[1], dist2[1]), ...))"

        In that specifically case, we can use DFS to find the shortest path
        starting from u to all nodes, because in this graph each node can have
        at most one outgoing edge. We can see intuitively that if every node has
        at most one outgoing edge, there can only be one path from a node to any
        other node.

        We can only have one branch as per our problem. So, DFS works for our
        use case to find the shortest distance from a node to all other nodes.

        The idea is to run DFS starting from both nodes to find the distance for
        all nodes. Then calculate the minimum maximum distance.
        """
        graph = defaultdict(list)

        for u, v in enumerate(edges):
            if v != -1:
                graph[u].append(v)

        def dfs(u, distance, node):
            if u in visited:
                return

            visited.add(u)
            dist[node][u] = distance

            for v in graph[u]:
                dfs(v, distance + 1, node)

        n = len(edges)
        dist = [[float("inf")] * n for _ in range(2)]

        visited = set()
        dfs(node1, 0, 0)

        visited = set()
        dfs(node2, 0, 1)

        print(dist)

        min_max_distance = float("inf")
        ans = -1

        for i in range(n):
            if min_max_distance > max(dist[0][i], dist[1][i]):
                ans = i
                min_max_distance = max(dist[0][i], dist[1][i])

        return ans

    # BFS optimized solution. Beats 87.78%
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        """
        It's given to us an array of edges and two nodes. Our task is to find a
        node that are reachable by both nodes (node1 and node2) and the maximum
        between the distance from node1 to that node, and from node2 to that
        node is minimized
        "(min(max(dist1[0], dist2[0]), max(dist1[1], dist2[1]), ...))"

        To calculate the distance from a node to all other, the best way is to
        use BFS algorithm, which does a level-wise iteration of the graph,
        guarantying the shortest path.

        The idea is to run BFS starting from both nodes to find the distance for
        all nodes. Then calculate the minimum maximum distance.

        Optimization: we don't need to create a list of adjacency because each
        node has at most one outgoing edge, which are already represented by the
        `edges` array. We can also remove the for loop inside the BFS, for
        the same reason. With this optimization, we go from 33.48% to 87.78%.
        """

        def bfs(start):
            queue = deque([(start, 0)])
            dist = [-1] * n

            v = 0

            while queue:
                u, step = queue.popleft()

                dist[u] = step
                v = edges[u]

                if v != -1 and dist[v] == -1:
                    queue.append((v, step + 1))

            return dist

        n = len(edges)

        dist1 = bfs(node1)
        dist2 = bfs(node2)

        min_max_distance = float("inf")
        ans = -1

        for i in range(n):
            if dist1[i] != -1 and dist2[i] != -1:
                curMax = dist1[i] if dist1[i] > dist2[i] else dist2[i]
                if min_max_distance > curMax:
                    ans = i
                    min_max_distance = curMax

        return ans


a = Solution()
print(a.closestMeetingNode(edges=[2, 2, 3, -1], node1=0, node2=1))
print(a.closestMeetingNode(edges=[1, 2, -1], node1=0, node2=2))
print(a.closestMeetingNode(edges=[4, 3, 0, 5, 3, -1], node1=4, node2=0))
print(a.closestMeetingNode(edges=[4, 4, 4, 5, 1, 2, 2], node1=1, node2=1))
