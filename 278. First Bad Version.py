# https://leetcode.com/problems/first-bad-versions

class Solution:
    def firstBadVersion(self, n):
        low = 1
        mid = (low + n) // 2
        while low <= n:
            if isBadVersion(mid):
                n = mid - 1
            else:
                low = mid + 1
            mid = (low + n) // 2
        return n + 1
