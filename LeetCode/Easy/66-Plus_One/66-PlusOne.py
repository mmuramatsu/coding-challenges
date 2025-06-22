class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        reminder = True

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9 and reminder:
                digits[i] = 0
            elif reminder == True:
                digits[i] += 1
                reminder = False
                break

        if reminder:
            digits = [1] + digits

        return digits


a = Solution()
print(a.plusOne([1, 2, 3]))
print(a.plusOne([4, 3, 2, 1]))
print(a.plusOne([9]))
print(a.plusOne([9, 0]))
