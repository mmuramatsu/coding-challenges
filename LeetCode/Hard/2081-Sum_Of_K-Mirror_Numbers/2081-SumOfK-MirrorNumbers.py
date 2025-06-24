class Solution:
    def kMirror(self, k: int, n: int) -> int:
        """
        Given an integer `k` and integer `n`, our task is to find the sum of the
        `n`-th numbers that are palindrome in both base-10 and base-`k`.

        First thought is to brute-force every single number and check if they
        are palindrome in both bases, but this will lead us to a TLE as this
        numbers can go too far. The idea is to restrict the space of search by
        checking only the palindromes in base-10.

        For this, we need to make a way to generate this palindromes numbers in
        order. There're two types of palindromes, the odd-length and
        even-length. To make a odd-length, we need to mirror the string without
        repeting the middle term, for example, the number "123" can form this
        odd-length palindrome "12321" ("123" + "21" or `s + s[:-1][::-1]`).

        To form a even-length palindrome, we just mirror the whole string, for
        example, the number "123" form this palindrome "123321" ("123" + "123"
        or `s + s[::-1]`).

        It's important to notice that an odd-length palindrome is always shorter
        than a even-length palindrome for a specific range of digits. To
        generate the numbers in order we're going to define a variable
        `range_digits = 1`, that will tell us which range we are generating the
        numbers. The idea is to run two for loops in the range
        [range_digits, range_digits*10]. The odd-length palindromes and the
        even-length palindromes will be handle by the first and second loop,
        respectively.

        Let's make an example to make it clear. We start with
        `range_digits = 1`, so the first loop will run in the range [1,10],
        which will generate the following palindromes [1,2,3...,9]. Then, we
        start the second loop, that will run in the same range and generate the
        following palindromes [11,22,33,...,99]. Finally we multiply
        `range_digits` by 10 to prepare for the next round. The next round, the
        first loop will return [101,111,121,...,191] and the second
        [1001,1111,1221,...,1991]. This will repeat until we get the required
        sum.

        Once we have the palindrome in base-10, let's call `num`, we check if
        this number is palindrome in base-`k` by converting this to base-`k`. We
        simply store the result of `num % k` in a list and divide
        `num //= base`. At the end of this process we have the inverse of the
        number in base-`k`, so we return the inverse.

        If `base_k == base_k[::-1]` is True, it means that this `num` is
        palindrome in both bases, so we add to the sum.
        """
        def to_base_k(num, base):
            if num == 0:
                return "0"

            base_k = []

            while num > 0:
                base_k.append(str(num % base))
                num //= base

            return "".join(base_k[::-1])

        count = 0
        ans = 0
        range_digits = 1

        while count < n:
            # Odd-lenght palindromes
            for i in range(range_digits, range_digits*10):
                s = str(i)
                palindrome = "".join([s, s[:-1][::-1]])
                num = int(palindrome)
                base_k = to_base_k(num, k)
                if base_k == base_k[::-1]:
                    count += 1
                    ans += num
                    if count == n:
                        return ans

            # Even-lenght palindromes
            for i in range(range_digits, range_digits*10):
                s = str(i)
                palindrome = "".join([s, s[::-1]])
                num = int(palindrome)
                base_k = to_base_k(num, k)
                if base_k == base_k[::-1]:
                    count += 1
                    ans += num
                    if count == n:
                        return ans

            range_digits *= 10

        return ans

a = Solution()
print(a.kMirror(k = 2, n = 5))
print(a.kMirror( k = 3, n = 7))
print(a.kMirror(k = 7, n = 17))