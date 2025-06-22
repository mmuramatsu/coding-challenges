class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        """
        Our task is to find the k-th number in the range [1, n] in
        lexicographical order.

        As the constraints are up to 10^9 we can't solve this in O(N) without a
        TLE. So we need to use a way to skip as many number as we can.

        First, we need to visualize this problem as a tree problem, in which the
        nodes are organized in the following way:

                    1
                 /  |  \
                10 11  12 ...
                |
                100 ...
                |
                1000 ...

        To solve this, we need to find a way to count how many nodes we have
        under one branch, in that way we can find the right node that we are
        looking for without needing to look at every single number.

        Let's define a helper function `count_nodes_under` to count how many
        nodes are under the node `root`. The idea is simple, we know how many
        number we have in the interval [a,b[, by doing "b - a". So if we want to
        know how many nodes are under the branch 1, which is {10,11,12,...,19},
        we need to find how many number are in [10,20[, which is "20 - 10 = 10".
        We just need to be carefull to not pass n, so the upper_limit needs to
        be the "min(n+1, b)".

        The idea of this function is simple, we receive a variable `root`, which
        we want to find how many nodes there under this root and define `start`
        of the interval as the root and the `end` of the interval as `root + 1`.
        While "start <= n", count will receive `min(n+1, end) - start`, then we
        multiply both `start` and `end` by 10. At the end of this `count` will
        have the number that we are looking for.

        Now, to find the exactly number that we are looking for, we can use a
        binary search-like strategy. Starting on the branch `curr=1`, we want
        the number of nodes under this branch, let's say `count`. If
        `k >= count`, means that the k-th number is not in this branch, so we
        move on to the next one by doing `curr += 1`. We also need to subtract
        count from k, because we already "count" the nodes that are in branch 1.
        If `k < count`, means that the k-th node are in this branch, so we move
        down on the tree by doing `curr *= 10`. We also need to decrement k by
        one to count the root of the branch that we moved on. When `k == 0`, we
        are at the node that we a looking for, so we return this.

        The outer while loop will run in the worst case O(log(N)) times, as we
        have two options, move to the next branch of move deeper. The helper
        function that we define also runs in O(log(N)), as we always move deeper
        in the tree to find the count. As the function is in the outer loop, the
        total complexity is O((log(N))^2).
        """

        def count_nodes_under(root):
            count = 0
            start = root
            end = root + 1

            while start <= n:
                count += min(n + 1, end) - start
                start *= 10
                end *= 10

            return count

        curr_branch = 1
        # This decrement is to count the node 1 that we are starting.
        k -= 1

        while k > 0:
            count = count_nodes_under(curr_branch)

            if k >= count:
                curr_branch += 1
                k -= count
            else:
                curr_branch *= 10
                k -= 1

        return curr_branch


a = Solution()
print(a.findKthNumber(n=13, k=2))
print(a.findKthNumber(n=1, k=1))
print(a.findKthNumber(n=2, k=2))
