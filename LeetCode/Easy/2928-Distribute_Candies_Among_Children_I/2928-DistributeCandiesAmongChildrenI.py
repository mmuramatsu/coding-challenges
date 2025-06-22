class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        """
        The problem ask us to find the number of ways to distribute N candies
        for K=3 kids such that no child gets more than `limit` candies.

        We know that c1 + c2 + c3 = n -> c2 + c3 = n - c1. The idea is to try
        every single valid number of candies for the first kid and calculate the
        number of ways we can distribute the remaining candies with the second
        and third kids.

        So, c1 can be valid only in the interval [0, min(n, limit)]. We have the
        rule that c1 <= limit, but if n < limit, then c1 <= n. So, we gonna loop
        through this interval.

        Not all c1 values will form a valid count. We need to check if
        n - c1 <= 2*limit, which can interpreted as "the remaning candies can be
        distributed between the two kids without break the limit rule".

        Let's focus on the equation "c2 + c3 = n - c1". Let R = n - c1 be the
        remaining number of candies for the second and third children. We need
        to find a integer solution to

            c2 + c3 = R
            0 <= c2 <= limit
            0 <= c3 <= limit

        For each choice of c2, we can determinet c3 as c3 = R - c2, so:

            0 <= c3 <= limit -> 0 <= R - c2 <= limit

        This inequality can be rewritten as:

            R - limit <= c2 <= R

        So, for c2 to be valid it must satisfy both inequalities. We can say
        that c2 must be within the intersection of [0, limit] and
        [R - limit, R], which is [max(0, R - limit), min(limit, R)], so:

            max(0, R - limit) <= c2 <= min(R, limit)

        We know that the number of integer values in a interval [a,b] is
        b - a + 1. So the number of valid integers for c2 is:

            min(R, limit) - max(0, R - limit) + 1

        Let's replace R = n - c1.

            min(n - c1, limit) - max(0, n - c1 - limit) + 1

        For a fixed c1, with this formula we can calculate the number of ways to
        distribute n - c1 candies to the last two kids.
        """
        ans = 0

        for c1 in range(min(n, limit) + 1):
            if n - c1 <= 2 * limit:
                ans += min(limit, n - c1) - max(0, n - c1 - limit) + 1

        return ans

    def distributeCandies1(self, n: int, limit: int) -> int:
        """
        The problem ask us to find the number of ways to distribute N candies
        for K=3 kids such that no child gets more than `limit` candies.

        The idea here is to brute force each possible value for c1, c2 and c3,
        where c1 + c2 + c3 == n.

        So, c1 can be valid only in the interval [0, min(n, limit)]. We have the
        rule that c1 <= limit, but if n < limit, then c1 <= n. So, we gonna loop
        through this interval.

        If "n - c1 <= 2 * limit", then it's possible to distribute "n - c1"
        candies between two kids without breaking limit rule.

        Similarly , c2 can be valid only in the interval
        [0, min(n - c1, limit)]. Also, "n - c1 - c2 <= limit" needs to be true,
        which means, that the remaining candies are less or equal to the limit
        to be distributed to the thrid kid.

        So, c3 can be valid only in the interval [0, n - c1 - c2]. If at this
        point, c1 + c2 + c3 = n, then we have a valid combination, so we add one
        to the answer.
        """
        ans = 0

        for c1 in range(min(n, limit) + 1):
            if n - c1 <= 2 * limit:
                for c2 in range(min(n - c1, limit) + 1):
                    if n - c1 - c2 <= limit:
                        for c3 in range(n - c1 - c2 + 1):
                            if c1 + c2 + c3 == n:
                                ans += 1

        return ans


a = Solution()
print(a.distributeCandies(n=5, limit=2))
print(a.distributeCandies(n=3, limit=3))
