class Solution:
    def minMaxDifference(self, num: int) -> int:
        """
        We're given an integer `num` where we can choose one digit ([0,9]) and
        replace all the repetitions of this digit for other digit, or even for
        itself. The problem asks us to return the difference between the maximum
        and the minimum by remapping exactly one digit.

        For this task, it's easy to transform `num` in a string and after we
        remap the digit we transform to integer again.

        To get the maximum, we need to find the most significant digit other
        than "9". For example, if `num="99545"`, the most significant digit
        different than "9" is `nums[2]="5"`. If we replace all occurencies of
        "5" by "9", we get `maximum="99949"`, which is the maximum we can get by
        remap one digit.

        As `num` is a valid integer, to get the minimum we just need to remap
        the first digit to "0". In the following example, if we remap `num[0]`
        to "0", we get `minimum="00545"`. When we transform this in integer we
        have `minimum=545`.

        We just need to return the difference between the maximum and minimum.
        """
        str_num = str(num)
        n = len(str_num)

        i = 0
        while i < n and str_num[i] == "9":
            i += 1

        if i < n:
            maximum = str_num.replace(str_num[i], "9")
        else:
            maximum = str_num

        minimum = str_num.replace(str_num[0], "0")

        return int(maximum) - int(minimum)


a = Solution()
print(a.minMaxDifference(num=11891))
print(a.minMaxDifference(num=90))
print(a.minMaxDifference(num=9999))
