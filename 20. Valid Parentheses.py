# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for bracket in s:
            if bracket in ('(', '{', '['):
                stack.append(bracket)
            else:
                if not stack:
                    return False
                last_br = stack.pop()
                if bracket == ']' and last_br != '[':
                    return False

                if bracket == ')' and last_br != '(':
                    return False

                if bracket == '}' and last_br != '{':
                    return False
        if stack:
            return False

        return True
