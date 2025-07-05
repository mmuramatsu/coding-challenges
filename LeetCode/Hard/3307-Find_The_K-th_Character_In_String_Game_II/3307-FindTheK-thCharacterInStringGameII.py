class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        k -= 1
        t = 0

        current_len = 1
        while current_len <= k:
            current_len *= 2
            t += 1

        final_char = ord("a")

        while current_len > 1:
            current_len //= 2
            t -= 1

            if k >= current_len:
                k -= current_len
                if operations[t] == 1:
                    final_char += 1

                    if final_char > ord("z"):
                        final_char = 97

        return chr(final_char)
