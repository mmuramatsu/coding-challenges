from collections import defaultdict, deque


class Solution:
    # BFS + Bipartite graph solution. Beats 69.53%.
    def maxTargetNodes(
        self, edges1: list[list[int]], edges2: list[list[int]]
    ) -> list[int]:
        """
        We reaceive two trees (undirected graphs) and our task is to add one new
        edge linking tree1 with tree2 that maximizes the number of target nodes
        for each node in the tree1.

        Consider a target node of u a node v that needs an even number of steps
        to get to this node.

        So, our answer will be an array `ans` of length n (len(graph1)) where
        `ans[i]` is the maximum number of target nodes starting from node i
        after adding a single new edge that links tree1 to tree2.

        We know that trees are acyclic graphs and follow a hierarchy structure.
        Based on that, we can transform this graph into Bipartite Graphs, which
        is a graph whose nodes can be divided into two disjoint sets.

        Our task is basically to divide the nodes of the tree into two groups, the
        ones that need even steps and the ones that need odd steps. We can do
        this by running a BFS starting from any node and classify each node in
        even and odd.

        It's interesting that we can start from any nodes and the groups will be
        the same. For example, the tree:

        0
        | \
        1 2

        If we start from node zero the group one, with the nodes that need even
        steps will be {0}, and the group two, that needs an odd number of steps,
        {1,2}. Now, let's start from node one, the groups will be one={1,2} and
        two={0}, the same from before, but inverted. So, if we want to know how
        much target nodes we have starting from node i, we just need to look at
        the length of the group that i belongs.

        So, we need to run BFS for both trees. For tree2 we need to find the
        maximum number of target nodes, by doing
        `max_target = max(len(group1), len(group2))`.This number will be added
        to each node of tree1. For each node of tree1 we check which group it
        belongs and add the length of their group to ans. It will be,
        `ans[i] = len(group) + max_target`.
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

        def bfs(node, graph):
            even = set()
            odd = set()
            queue = deque([(node, 0, -1)])

            while queue:
                u, step, par = queue.popleft()

                if step & 1:
                    odd.add(u)
                else:
                    even.add(u)

                for v in graph[u]:
                    if v != par:
                        queue.append((v, step + 1, u))

            return even, odd

        even1, odd1 = bfs(0, graph1)
        even2, odd2 = bfs(0, graph2)

        max_target = max(len(even2), len(odd2))

        ans = [0] * n

        for i in range(n):
            if i in even1:
                ans[i] = len(even1) + max_target
            else:
                ans[i] = len(odd1) + max_target

        return ans


a = Solution()
print(
    a.maxTargetNodes(
        edges1=[[0, 1], [0, 2], [2, 3], [2, 4]],
        edges2=[[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]],
    )
)
print(
    a.maxTargetNodes(
        edges1=[[0, 1], [0, 2], [0, 3], [0, 4]], edges2=[[0, 1], [1, 2], [2, 3]]
    )
)
