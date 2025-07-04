class Solution:
    # Math solution. Beats 100%
    def kthCharacter(self, k: int) -> str:
        return chr(ord("a") + (k - 1).bit_count())
        return chr(ord("a") + sum(map(int, list("{0:b}".format(k - 1)))))

    # Divide and conquer solution. Beats 100%.
    def kthCharacter1(self, k: int) -> str:
        k -= 1

        current_len = 1
        while current_len <= k:
            current_len *= 2

        final_char = ord("a")

        while current_len > 1:
            current_len //= 2

            if k >= current_len:
                k -= current_len

                final_char += 1
        return chr(final_char)

    # Simulation solution. Beats 58.54%.
    def kthCharacter1(self, k: int) -> str:
        s = "a"

        while len(s) < k:
            transform = [s]
            for c in s:
                char = chr(ord(c) + 1)
                if char == "{":
                    char = "a"

                transform.append(char)

            s = "".join(transform)

        print(s)

        return s[k - 1]


a = Solution()
print(a.kthCharacter(5))
print(a.kthCharacter(10))
print(a.kthCharacter(257))
