class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        """
        The problem ask us to find the number of ways to distribute N candies
        for K=3 kids such that no child gets more than `limit` candies.

        First we going to solve the problem "Distribute N candies into K bins"
        (without any restriction). There's a theorem called "Stars and bars
        theorem" that prove exactly that. The solution for that problem is given
        by the binomial coefficient:

            C(n + k - 1, k - 1)  (which is "n+k-1 choose k-1")

        In our case will be, for k=3:

            C(n + 2, 2) = (n+2)!  = (n+2) . (n+1) . n . (n-1)...
                          -------   ----------------------------
                          2 . n!          2 . n . (n-1) ....

        We can cancel "n . (n-1)..." term:

             C(n + 2, 2) = (n+1) . (n+2)
                           --------------  (1)
                                 2

        With this, we have a way to calculate the number of ways to distribute N
        candies for 3 kids without restrictions. The idea now is to use Set
        Theory to subtract the invalid configurations (kids with more than
        `limit` of candies) from the total.

        Let's consider the total number of ways to distribute N candies for k
        kids as U (U = C(n+2, 2)). Let V be the set of the valid counts and I
        the invalid counts for our problem. We can say:

            U = V + I -> V = U - I, which is the answer.

        So, our task now is to calculate the I set. The I set will be compose of
        the counts where some kid receive more than `limit` of candies. So, let
        A_1 be the set where the first kid receive more than `limit` of candies.
        In the same way, let A_2 and A_3, for the second and third kid,
        respectively.

        We can say that I = A_1 U A_2 U A_3. Let's calculate A_i. We know that:

            U -> { x_1 + x_2 + x_3 = N -> C(n + 2, 2)

        Let A_i be:

            A_i -> { x_1 + x_2 + x_3 = N, where x_i > limit (2)

        Suppose that A_1 kid has more than `limit`, then:

            x_1 > limit

        The minimum value greater than the limit is:

            x_1 = limit + 1 -> x_1 - (limit + 1) = 0

        Let subtract "limit+1" in both sides of (2):

            A_1 -> {x_1 - (limit + 1) + x_2 + x_3 = N - (limit + 1)

        Let "x_1 - (limit + 1) = y_1", so:

            A_1 -> {y_1 + x_2 + x_3 = N - (limit + 1) -> C(n-(limit + 1), 2)

        Using (1) we can calculete A_1, A_2 and A_3 just by changing the n value
        to "n-(limit + 1)". But, according to the principle of
        inclusion-exclusion, we need to calculate the intersections of A_1, A_2
        and A_3 to properly subtract from U.

        Similarly, let consider that the first and second kids has more the
        `limit`, so we can say:

            A_12 -> {x_1 - (limit + 1) + x_2 - (limit + 1) + x_3 = N - 2 * (limit + 1)
            A_12 -> {y_1 + y_2 + x_3 = N - 2 * (limit + 1) -> C(n-2*(limit+1), 2)

        With this we can calculate the sets A_12, A_13 and A_23. Now we can
        repeat the same idea to calculate A_123.

            A_123 -> {x_1 - (limit + 1) + x_2 - (limit + 1) + x_3 - (limit + 1) = N - 3 * (limit + 1)
            A_123 -> {y_1 + y_2 + y_3 = N - 3 * (limit + 1) -> C(n-3*(limit+1), 2)

        Finally, our answer will be:

            V = U - I
            V = C(n+2, 2) - 3*C(n-(limit + 1), 2) + 3*C(n-2*(limit+1), 2) - C(n-3*(limit+1), 2)

        We need to subtract "3*A_i", becausa there's three cases A_1, A_2 and
        A_3. The same for "3*A_ij", due to the cases A_12, A_13 and A_23.
        """

        def combination(n):
            if n < 0:
                return 0

            return ((n + 1) * (n + 2)) // 2

        U = combination(n)
        A_i = 3 * combination(n - (limit + 1))
        A_ij = 3 * combination(n - 2 * (limit + 1))
        A_123 = combination(n - 3 * (limit + 1))

        return U - A_i + A_ij - A_123


a = Solution()
print(a.distributeCandies(n=5, limit=2))
print(a.distributeCandies(n=3, limit=3))
