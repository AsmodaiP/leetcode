# https://leetcode.com/problems/longest-repeating-character-replacement/
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        size = 0
        dic = {}
        start = 0
        repeat = 0

        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i], 0) + 1

            repeat = max(repeat, dic[s[i]])
            len_of_sequence = i-start+1
            if len_of_sequence - repeat > k:
                dic[s[start]] -= 1
                start += 1
            size = max(i-start+1, size)
        return size
