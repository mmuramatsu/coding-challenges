from collections import defaultdict


class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        freq = defaultdict(int)

        reminder = 0

        for ans in answers:
            if freq[ans] % (ans + 1) == 0:
                reminder += ans
            else:
                reminder -= 1

            freq[ans] += 1
            # print("reminder: ", reminder)

        return len(answers) + reminder


a = Solution()

print(a.numRabbits([1, 1, 2]))
print(a.numRabbits([10, 10, 10]))
print(a.numRabbits([0, 0, 1, 1, 1]))
print(a.numRabbits([2, 2, 2]))
print(a.numRabbits([2, 2, 2, 2]))
print(a.numRabbits([2, 2, 2, 2, 2]))
