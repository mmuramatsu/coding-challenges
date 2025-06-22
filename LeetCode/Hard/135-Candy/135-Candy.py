class Solution:
    def candy(self, ratings: list[int]) -> int:
        """
        We need to distribute candies to n kids, following two rules.
            1. Each child must have at least one candy;
            2. Children with a higher rating get more candies than their
            neighbors.

        Let `ans` by the array that store the number of candies of each kid. We
        initialize this array with 1 in all positions, fulfilling the first
        rule.

        Now we going to run through the array verifying the relation
        between the neighbor on the left of each kid. If the rating of the kid i
        is greater than the kid on the left (i-1), then the ith kid need to
        receive more than the kid on the left. So, the ith kid receive
        `ans[i-1] + 1`.

        Next step is to verify the relation between the neighbor on the right of
        each kid. Starting on the end of the array, if the rating of the ith kid
        is greater than the kid on the right (i+1), then the ith kid need to
        receive more candies than your neighbor on the right, but we need to
        make sure that we didn't break the first pass that we did earlier.

        So, the ith kid will receive the max(ans[i], ans[i+1] + 1). If
        ans[i] > ans[i+1] + 1, then the ith kid already receive more candies
        than the neighbor on the right, so we don't need to do anything.
        Otherwise, the neighbor on the right is receiving more with a lower
        rating, so ans[i] = ans[i+1] + 1.

        The answer will be the sum of our ans array.
        """
        n = len(ratings)
        ans = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                ans[i] = ans[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                # ans[i] = max(ans[i], ans[i + 1] + 1)
                ans[i] = ans[i] if ans[i] > ans[i + 1] + 1 else ans[i + 1] + 1

        return sum(ans)


a = Solution()
print(a.candy([1, 0, 2]))
print(a.candy([1, 2, 2]))
print(a.candy([1, 3, 2, 2, 1]))
print(a.candy([1, 2, 87, 87, 87, 2, 1]))
