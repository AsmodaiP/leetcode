class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_dict = {}
        ans = []
        for let in p:
            p_dict[let] = p_dict.get(let, 0) + 1
        left = 0
        window_dict = {}

        for right, val in enumerate(s):
            window_dict[val] = window_dict.get(val, 0) + 1
            if right >= len(p) - 1:
                if window_dict == p_dict:
                    ans.append(left)
                if window_dict[s[left]] == 1:
                    del window_dict[s[left]]
                else:
                    window_dict[s[left]] -= 1
                left += 1
    
        return ans


sol = Solution()
print(sol.findAnagrams("cbaebabacd", "abc"))
