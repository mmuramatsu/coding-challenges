from collections import defaultdict


class Solution:
    # DFS + Connected components solution. Beats 49.64%.
    def smallestEquivalentString1(self, s1: str, s2: str, baseStr: str) -> str:
        """
        Given two strings s1 and s2, where s1[i] and s2[i] are equivalent, which
        means that s1[i] can be replaced by s2[i] or s2[i] by s1[i]. Our task to
        return the lexicographically smallest equivalent string of `baseStr` by
        using the equivalency information from s1 and s2.

        The idea to solve this problem is to represent this equivalency as a
        graph, so the letters that are equivalent will be at the same connected
        component. First, we build our adjacency list where each char s1[i] and
        s2[i] will have an edge connecting them.

        For example, suposse we have s1="acd" and s2="bbe". So, the equivalency
        will be 'a' == 'b', 'b' == 'c' and 'd' == 'e'. In that case, our graph
        will be:

            a --- b --- c         d --- e

        which maintain the equivalencies described above and make clear the idea
        of connected components in which {a,b,c} is a component and {d,e} the
        other.

        To find which nodes are part of each component we can use a simple DFS.
        We need to maintain two sets, one to mark the nodes that we have already
        visited and other to mark the member of the current component. Every
        time the visit a node we add this node in both sets.

        When the DFS ends, we have all nodes that are member of the current
        component, we save this and try to run the DFS for other node to find
        other component. We can use a Dict to store the minimum equivalency for
        each char in this component.

        The problem ask us to rewrite the string `baseStr` using the
        lexicographically smallest equivalent characters. So for each character
        c in `baseStr`, if c is the `visited` set, meaning c is part of our
        graph, we replace c by the minimum equivalency finded in our Dict.
        Otherwise, c will still be c in the final string.
        """
        ans = ""

        graph = defaultdict(set)

        for i in range(len(s1)):
            graph[s1[i]].add(s2[i])
            graph[s2[i]].add(s1[i])

        def dfs(u):
            if u in visited:
                return

            visited.add(u)
            aux.add(u)

            for v in graph[u]:
                dfs(v)

        visited = set()
        min_equivalent = {}

        for k in graph.keys():
            aux = set()
            dfs(k)

            if aux:
                min_char = min(aux)
                for c in aux:
                    min_equivalent[c] = min_char

        for c in baseStr:
            if c in visited:
                ans += min_equivalent[c]
            else:
                ans += c

        return ans

    # Union-Find approach. Beats 96.50%
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        """
        Given two strings s1 and s2, where s1[i] and s2[i] are equivalent, which
        means that s1[i] can be replaced by s2[i] or s2[i] by s1[i]. Our task to
        return the lexicographically smallest equivalent string of baseStr by
        using the equivalency information from s1 and s2.

        This problem can be solved using Union-Find or Disjoint Set Union.
        Union-Find is a data structure that keeps track of a set of elements
        partitioned into a number of disjoint (non-overlapping) subsets. This
        data structure has two basic operations, `find(i)` which return the
        "representative" (or "root") of the set that element belongs to. If two
        elements have the same representative, they are in the same set. The
        other operation are `union(i, j)`, which merges two sets containing i
        and j into a single set.

        We can represent all the 26 characters using an array. The `parent`
        array start with every single position `parent[i] == i`, meaning that
        each character i is it's own root.

        In find operation we want to find the root of some set, so, we need to
        stop if `parent[i] == i` and return this. The idea to do so, is to
        recursive call `find(parent[i])` until the inverse condition is true,
        and then return `parent[i]`. We can make an optimization to flatten the
        tree. Imagine that we have this scenario "0 <- 1 <- 2 <- 3 <- 4", when
        we do `find(4)`, we need to run through all parents to get to 0, which
        can be a lot cost if we have a huge amount of parents (It's a O(N)
        operation). The optimization can be done by using the comeback of the
        recursive call to make the parents to point directly to the root, so
        we're needed to do this cost operation only once.

        The idea of the union operation is to simple make the root of i point to
        root of j. In our this case it's better to make the smallest as the
        root, so it will better to rewrite the `baseStr`.

        For each character s1[i] and s2[i], we perform a union of s1[i] and
        s2[i]. To reconstruct the `baseStr` we going to perform a find for each
        character in `baseStr`.
        """
        ans = ""

        parent = [i for i in range(26)]

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])

            return parent[i]

        def union(i, j):
            p_i, p_j = find(i), find(j)

            if p_i != p_j:
                if p_i < p_j:
                    parent[p_j] = p_i
                else:
                    parent[p_i] = p_j

        for i in range(len(s1)):
            union(ord(s1[i]) - 97, ord(s2[i]) - 97)

        for c in baseStr:
            ans += chr(find(ord(c) - 97) + 97)

        return ans


a = Solution()
print(a.smallestEquivalentString(s1="zz", s2="ba", baseStr="zz"))
print(a.smallestEquivalentString(s1="parker", s2="morris", baseStr="parser"))
print(a.smallestEquivalentString(s1="hello", s2="world", baseStr="hold"))
print(a.smallestEquivalentString(s1="leetcode", s2="programs", baseStr="sourcecode"))
