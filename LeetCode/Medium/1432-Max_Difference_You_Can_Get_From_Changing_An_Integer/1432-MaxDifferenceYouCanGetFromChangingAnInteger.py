class Solution:
    def maxDiff(self, num: int) -> int:
        """
        We're given a integer `num` and we need to pick a digit `x`
        (0 <= x <= 9) and remap all the occurencies in `num` to a digit `y`
        (0 <= y <= 9). We need to do this twice, creating two numbers `a` and
        `b`. Our task is to find the maximum of `a - b`.

        As we need to find the maximum of the difference of `a` and `b`, we need
        to find the maximum number that we can get in `a` and the minimum in `b`
        by remapping a digit. First we transform `num` into string as it's a lot
        easier to replace digits in this form.

        To get the maximum we need that the most significant digit different
        than "9" to be remapped to "9". For example `num=987`, the maximum we
        can get is `a=997`. If all digits are  "9", we just leave in that way.
        (can be interpreted as "replacing '9' by '9'.")

        To find the minimum we need first to verify the first digit of `num`. We
        can't remap the first digit to "0" because the number can't have leading
        zeroes, so if the first digit is different than "1", we remap the first
        digit to "1". For example `num=987`, the minimum we can get is `b=187`.

        If the first digit is "1", then we need to find the next digit that is
        different than "1" or "0" to remap to "0". For example `num=109`, the
        minimum we can get is `b=100`.
        """
        str_num = str(num)
        n = len(str_num)

        i = 0
        while i < n and str_num[i] == "9":
            i += 1

        if i < n:
            a = str_num.replace(str_num[i], "9")
        else:
            a = str_num

        if str_num[0] != "1":
            b = str_num.replace(str_num[0], "1")
        else:
            i = 0
            while i < n and (str_num[i] == "1" or str_num[i] == "0"):
                i += 1

            if i < n:
                b = str_num.replace(str_num[i], "0")
            else:
                b = str_num

        return int(a) - int(b)


a = Solution()
print(a.maxDiff(num=555))
print(a.maxDiff(num=9))
print(a.maxDiff(num=9288))
print(a.maxDiff(num=1101057))
print(a.maxDiff(num=123456))
