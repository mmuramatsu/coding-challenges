from collections import defaultdict, deque


class Solution:
    # DFS solution. Beats 7.09%
    def maxTargetNodes1(
        self, edges1: list[list[int]], edges2: list[list[int]], k: int
    ) -> list[int]:
        """
        We reaceive two trees (undirected graphs) and our task is to add one new
        edge linking tree1 with tree2 that maximizes the number of target nodes
        for each node in the tree1.

        Consider a target node of u a node v that needs k or less steps to get
        to this node.

        Our answer will be a n (len(graph1)) array. Let `ans[i]` be the maximum
        number of nodes targets starting from node i.

        The idea to use DFS to find the target nodes from a starting node.

        First, for each node u in tree2 we find how many nodes v can be arrived
        in k-1 steps or less. It's because if a node in tree1 is connected to a
        node in tree2 that has x nodes reachable within k-1 steps, then from the
        tree1 node, those x nodes in tree2 become reachable within k steps (by
        going through the new edge). To calculete this we need to reset our
        visited set after each DFS call completed. We then, save the greater
        value founded in `max_target`.

        Second, we do the same for tree1 but now for a k steps. The idea is to
        count how many target nodes are in the tree1 starting from each node of
        tree1. The we sum the result with the `max_target` founded before, which
        cen be interpreted as "there's x targets nodes on tree1 starting in i
        plus `max_target` if we add a single new edge that link tree1 to tree2."
        """
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)

        for u, v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)

        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)

        n = len(graph1)
        m = len(graph2)

        def dfs(node, step, graph):
            if node in visited:
                return

            if step <= target_step:
                nonlocal target
                target += 1

            visited.add(node)

            for neighbor in graph[node]:
                dfs(neighbor, step + 1, graph)

        max_target = 0
        for i in range(m):
            target = 0
            target_step = k - 1
            visited = set()
            dfs(i, 0, graph2)

            max_target = target if target > max_target else max_target

        ans = [0] * n

        for i in range(n):
            target = 0
            target_step = k
            visited = set()
            dfs(i, 0, graph1)
            ans[i] = target + max_target

        return ans

    # BFS solution. Beats 55.12%
    def maxTargetNodes(
        self, edges1: list[list[int]], edges2: list[list[int]], k: int
    ) -> list[int]:
        """
        We reaceive two trees (undirected graphs) and our task is to add one new
        edge linking tree1 with tree2 that maximizes the number of target nodes
        for each node in the tree1.

        Consider a target node of u a node v that needs k or less steps to get
        to this node.

        Our answer will be a n (len(graph1)) array. Let `ans[i]` be the maximum
        number of nodes targets starting from node i.

        The idea to use BFS to find the target nodes from a starting node.

        First, for each node u in tree2 we find how many nodes v can be arrived
        in k-1 steps or less. It's because if a node in tree1 is connected to a
        node in tree2 that has x nodes reachable within k-1 steps, then from the
        tree1 node, those x nodes in tree2 become reachable within k steps (by
        going through the new edge). To calculete this we need to reset our
        visited set after each DFS call completed. We then, save the greater
        value founded in `max_target`.

        Second, we do the same for tree1 but now for a k steps. The idea is to
        count how many target nodes are in the tree1 starting from each node of
        tree1. The we sum the result with the `max_target` founded before, which
        cen be interpreted as "there's x targets nodes on tree1 starting in i
        plus `max_target` if we add a single new edge that link tree1 to tree2."

        In our BFS function we don't need to keep a visited set because we are
        dealing with trees. In the context of a BFS on a tree, by keeping track
        of the parent node during the traversal, we inherently prevent from
        immediately going back to the node you just came from. Since trees have
        no other cycles, this mechanism is sufficient to ensure you explore each
        new node only once along a given path from the starting node of the BFS.
        """
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)

        for u, v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)

        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)

        n = len(graph1)
        m = len(graph2)

        def bfs(node, graph, target_step):
            queue = deque([(node, 0, -1)])
            nonlocal target

            while queue:
                u, step, par = queue.popleft()

                if step <= target_step:
                    target += 1

                for v in graph[u]:
                    if v != par and step + 1 <= target_step:
                        queue.append((v, step + 1, u))

        max_target = 0
        for i in range(m):
            target = 0
            bfs(i, graph2, k - 1)

            max_target = target if target > max_target else max_target

        ans = [0] * n

        for i in range(n):
            target = 0
            bfs(i, graph1, k)
            ans[i] = target + max_target

        return ans


a = Solution()
print(
    a.maxTargetNodes(
        edges1=[[0, 1], [0, 2], [2, 3], [2, 4]],
        edges2=[[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]],
        k=2,
    )
)
print(
    a.maxTargetNodes(
        edges1=[[0, 1], [0, 2], [0, 3], [0, 4]], edges2=[[0, 1], [1, 2], [2, 3]], k=1
    )
)
