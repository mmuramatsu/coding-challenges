class Solution:
    # Beats 100%.
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        """
        Given a string `s`, an integer `k`, and a string `fill`, our task is to
        split this string into substrings of length `k`. If the last substring
        is less than `k` characters long, we need to add the string `fill` at
        the end until it is of length `k`.

        The idea is to first add the necessary character to make
        `len(s) % k == 0`, then with a simple loop, we make the split. The
        amount of characters that we need to be add is `(k - (len(s) % k))`, so
        we create a string filled with `fill` of size `(k - (len(s) % k))`.

        Then, to make the answer we set a simple for loop with increment of k
        and append each trim the string in [i: i+k] interval.

        OBS: there are two main methods to append strings. The default one is to
        concatenate by use the operator "+". As strings in Python are immutable,
        the interpreter need to allocate a new space for each concatenation and
        copy all characters of some pair of strings to that new space, which can
        be cost in some situations. A better way to do concatenations in
        competitive programming is to use `join` method, which is generally more
        efficient for concatenating multiple strings as it calculates the total
        length of the resulting string once and allocates memory accordingly,
        minimizing reallocations and copying.
        """
        n = len(s)

        if n % k != 0:
            s = "".join([s, fill * (k - (n % k))])

        return [s[i : i + k] for i in range(0, n, k)]


a = Solution()
print(a.divideString(s="abcdefghi", k=3, fill="x"))
print(a.divideString(s="abcdefghij", k=3, fill="x"))
