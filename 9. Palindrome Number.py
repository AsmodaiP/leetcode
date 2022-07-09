# https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        result = 0
        original_x = x
        while x:
            x, y = divmod(x, 10)
            result = result * 10 + y

        return result == original_x


