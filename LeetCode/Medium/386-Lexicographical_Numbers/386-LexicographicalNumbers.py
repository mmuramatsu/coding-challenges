class Solution:
    # DFS solution. Beats 17.39%.
    def lexicalOrder1(self, n: int) -> list[int]:
        """
        Our task is to make an array with the numbers in range [1, n] in
        lexicographical order. This task needs to be done in O(N) time
        complexity with O(1) extra space.

        To accomplish this goal we can use DFS to run through the numbers in
        lexicographical order. The idea is to try to append every single digit
        from 0 to 9 at each step of the DFS. If we represent this as a tree, it
        will be something like this:

                    1
                 /  |  \
                10 11  12 ...
                |
                100 ...
                |
                1000 ...

        As the name says, Depth First Search will run through the deeply nodes
        first, maintaining the lexicographical order (order:
        {1,10,100,1000,...,101,...,11,...}). We just need to stop if the number
        is greater than n.

        To get the final sequence, we just need to call DFS for each number in
        range 1 to 9.
        """
        ans = []

        def dfs(number):
            if number > n:
                return

            ans.append(number)

            for i in range(10):
                dfs((number * 10) + i)

        for i in range(1, 10):
            dfs(i)

        return ans

    # Iterative solution. Beats 95.08%.
    def lexicalOrder(self, n: int) -> list[int]:
        """
        Our task is to make an array with the numbers in range [1, n] in
        lexicographical order. This task needs to be done in O(N) time
        complexity with O(1) extra space.

        We can do this in one for loop if we understand the logic behind the
        order. If we think this sequence as a tree, our goal is to run through
        the deeply nodes first, increment 10 times, then backtrack one digit,
        increment again, then backtrack again.(order:
        {1,10,100,1000,1001,...,1009,101,1010,...})

                    1
                 /  |  \
                10 11  12 ...
                |
                100 ...
                |
                1000 ...

        Let n=122, the first number to appers in the sequence is {1,10,100,...},
        so, let `cur` be the current number that we going to append in our
        sequence. Starting from `cur=1`, we can first multiply `cur` by 10 if
        `cur * 10 <= n`, otherwise we pass n.

        At this point, `cur=100`, now it's to increment, so we going to get
        {101,102,...,109}. If we continue doing this we going to have "110",
        which needs to be placed after "11" in our sequence. So, after we
        increment, while `cur % 10 == 0`, we need to divide the number by 10 (it
        need to be an will in because there's cases like "1999" that need a lot
        of division to make up the next number of the sequence. The sequence
        must be {...,1999,2,20,200,2000,...}, so we need to keep dividing until
        `cur % 10 == 0` is not true.)

        After the backtrack, `cur=11`, which can be multiplied by 10, so we do,
        getting `cur=110`. Then we increment again. When we reach `cur=119`, we
        need to backtrack again, so increment one and divide by 10, getting,
        `cur=12`. When we get to `cur=122`, which is equals to n, we need to
        backtrack right away, so we need a special condition to backtrack if
        `cur >= n`, going to the next number, which is `cur=13`.

        If we keep doing this algorithm, we will have all the sequence. Let's
        summarize this, starting from 1, (1) if it's possible to multiply by 10,
        do it. Otherwise, (2) increment. When the number becomes divisible by
        10, (3) we need to backtrack because we already tried every single digit
        possible. Finally, (4) the special condition to backtrack if we reach n.
        """
        ans = []
        cur = 1

        for _ in range(n):
            ans.append(cur)

            # (1) multiply by 10 if is possible
            if cur * 10 <= n:
                cur *= 10
            else:
                # (4) backtrack when reach n.
                if cur >= n:
                    cur //= 10

                # (2) increment
                cur += 1

                # (3) backtrack after tried every single digit
                while cur % 10 == 0:
                    cur //= 10

        return ans


a = Solution()
print(a.lexicalOrder(13))
print(a.lexicalOrder(2))
print(a.lexicalOrder(243))
print(a.lexicalOrder(122))
print(a.lexicalOrder(24))
