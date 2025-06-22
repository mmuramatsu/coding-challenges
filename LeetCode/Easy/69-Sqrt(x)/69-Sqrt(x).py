class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x

        while left <= right:
            mid = (left + right) // 2
            mid_squared = mid * mid

            if mid_squared == x:
                return mid
            elif mid_squared > x:
                right = mid - 1
            else:
                left = mid + 1

        return right


a = Solution()
print(a.mySqrt(9))
print(a.mySqrt(4))
print(a.mySqrt(8))
print(a.mySqrt(0))
