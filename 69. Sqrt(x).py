class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        while start <= end:
            mid = (start + end) >> 1
            if mid*mid <= x and (mid+1)*(mid+1) > x:
                return mid
            if mid * mid < x:
                start = mid+1
            else:
                end = mid - 1
        return end
