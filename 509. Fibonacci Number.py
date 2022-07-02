class Solution(object):
    def fib(self, n):
        def fibonach(n=0, prev_result=1, prev_prev_result=1, current_n=1, ):
            if n == 0:
                return 0
            if n == 1:
                return 1

            if current_n+1 == n:
                return prev_result
            current_n += 1
            new_result = prev_result + prev_prev_result

            return fibonach(n, new_result, prev_result, current_n)
        return(fibonach(n))

