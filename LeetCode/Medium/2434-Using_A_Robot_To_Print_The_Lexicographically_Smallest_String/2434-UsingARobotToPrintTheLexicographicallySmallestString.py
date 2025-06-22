from collections import Counter, deque


class Solution:
    # Stack + Map frequencies solution. Beats 32.44%.
    def robotWithString1(self, s: str) -> str:
        """
        It's given a string `s` and for each character `s[i]` we have two
        options to do:
            1. Append `s[i]` into a string `t`;
            2. Pop the last character of `t` and "print".

        We need to return the lexicographically smallest string that can be
        printed. The idea of this problem is that `t` will act as a stack and
        the answer is the best order to pop and push characters in the stack to
        get the lexicographically smallest string possible.

        The key point of this problem is to know what is the minimum character
        remaining in the string after we push one character in our stack.
        Suppose we have the s='za', when we push 'z' into our stack, in order to
        get the lexicographically smallest string possible, we can't pop 'z'
        from our stack and move to our answer because we have a character in `s`
        that are less than 'z'. So, we need to push the 'a' and then pop the two
        items, getting as answer 'az'.

        Our strategy here is to count the frequency of each character on the
        string and save in a Map. For each `c` in `s`, we push `c` into our
        stack and decrese the frequency of c on our Map.

        Next, we need to find the smallest char in our remaining string. We're
        doing this by running through 'a' to 'z' finding in our Map a frequency
        greater than 0, the first that we find is the smallest character in the
        remaining string.

        With the smallest character, we're going to look into our stack and pop
        elements from there while the top of our stack is less or equal to the
        smallest char. When this condition is false, it means that there is a
        character small in the remaining string than the character on the top of
        our stack, so we need to push more elements into our stack to proceed.

        We're going to repeat this until we run through all `s` and our stack is
        empty.
        """
        freq = Counter(s)
        n = len(s)

        i = 0
        stack = deque()
        ans = []
        small_char = "a"

        while i < n:
            stack.append(s[i])
            freq[s[i]] -= 1

            # Finding the smallest char remaining
            while small_char != "z":
                if freq[small_char] > 0:
                    break

                small_char = chr(ord(small_char) + 1)

            while stack and stack[-1] <= small_char:
                ans.append(stack.pop())

            i += 1

        return "".join(ans)

    # Stack + suffix minimums solution. Beats 90.00%.
    def robotWithString(self, s: str) -> str:
        """
        It's given a string `s` and for each character `s[i]` we have two
        options to do:
            1. Append `s[i]` into a string `t`;
            2. Pop the last character of `t` and "print".

        We need to return the lexicographically smallest string that can be
        printed. The idea of this problem is that `t` will act as a stack and
        the answer is the best order to pop and push characters in the stack to
        get the lexicographically smallest string possible.

        The key point of this problem is to know what is the minimum character
        remaining in the string after we push one character in our stack.
        Suppose we have the s='za', when we push 'z' into our stack, in order to
        get the lexicographically smallest string possible, we can't pop 'z'
        from our stack and move to our answer because we have a character in `s`
        that are less than 'z'. So, we need to push the 'a' and then pop the two
        items, getting as answer 'az'.

        Let n be the lenght of `s`, our strategy here is to precomputate the
        suffix minimums. We're going to create an array, where each position i
        store the lexicographically smallest character from [i, n]. So, if we
        want to know what is the smallest character in the remaining string, we
        just need to look into `min_char_suf[i+1]`.

        To build this array, initially we make every single position equals to
        the last character of `s`, then we're going to loop from n-2 to 0, and
        for each position we going to save the `min(s[i], min_char_suf[i+1])`.

        The smallest character in the remaing string can be found by doing
        `min_char_suf[i+1]`, but when i=n-1, we'll get an error. If we invert
        the logic, we avoid the necessity to check this edge case where
        `min_char_suf[i+1]` is out of bounds. The logic to make our answer is,
        first try to pop items from our stack and then push new elements into
        our stack.

        When this loop ends, we reached the end of `s`. If our stack is not
        empty, then there's no other way to deal with the remaining elements in
        our stack instead of pop in order. So, we simply pop elements from our
        stack until it's empty.
        """
        n = len(s)
        min_char_suf = [s[-1]] * n

        for i in range(n - 2, -1, -1):
            if s[i] < min_char_suf[i + 1]:
                min_char_suf[i] = s[i]
            else:
                min_char_suf[i] = min_char_suf[i + 1]

        ans = []
        stack = deque()
        i = 0

        while i < n:
            while stack and stack[-1] <= min_char_suf[i]:
                ans.append(stack.pop())

            stack.append(s[i])
            i += 1

        while stack:
            ans.append(stack.pop())

        return "".join(ans)


a = Solution()


print(a.robotWithString(s="zza"))
print(a.robotWithString(s="bac"))
print(a.robotWithString(s="bdda"))
print(a.robotWithString(s="bada"))
print(a.robotWithString(s="bydizfve"))
print(a.robotWithString(s="vzhofnpo"))
