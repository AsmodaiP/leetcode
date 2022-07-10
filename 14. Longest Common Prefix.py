class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        
        initial_string = strs[0]
        for i in range(len(strs)):
            current_string = strs[i]
            if len(initial_string) > len(current_string):
                initial_string = initial_string[:len(current_string)]
            for j in range(len(initial_string)):
                if initial_string[j] != current_string[j]:
                    initial_string = initial_string[:j]
                    break
        return initial_string