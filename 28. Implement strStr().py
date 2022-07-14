class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # return haystack.find(needle)
        if needle == '':
            return 0
        needle_len = len(needle)
        for i in range(len(haystack) - needle_len + 1):
            if haystack[i:i+needle_len] == needle:
                return i
        return -1