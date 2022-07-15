# https://leetcode.com/problems/length-of-last-word/

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        s = s.strip()
        if s == '':
            return 0
        return len(s.split(' ')[-1])