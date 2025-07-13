class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        if not edges:
            return 0

        edges.sort(key=lambda x: x[2])

        def check(x):
            graph = defaultdict(list)

            for u, v, w in edges:
                if w > x:
                    break
                graph[u].append(v)
                graph[v].append(u)

            def dfs(u):
                visited.add(u)

                for v in graph[u]:
                    if v not in visited:
                        dfs(v)

            visited = set()
            components = 0

            for u in range(n):
                if u not in visited:
                    components += 1
                    dfs(u)

            return components <= k

        low = 0
        high = edges[-1][2]
        ans = high

        while low <= high:
            mid = (high + low) // 2

            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
