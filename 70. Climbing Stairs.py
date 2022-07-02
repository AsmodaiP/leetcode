# https://leetcode.com/problems/climbing-stairs/
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def fibonacci_for_climb(n=0, prev_result=1, prev_prev_result=1, current_n=1):
            if n == 0:
                return 1
            if n == 1:
                return 1

            new_result = prev_result + prev_prev_result
            if current_n+1 == n:
                return new_result
            current_n += 1

            return fibonacci_for_climb(n, new_result, prev_result, current_n)
        return fibonacci_for_climb(n)
