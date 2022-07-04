# https://leetcode.com/problems/unique-paths/

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        paths = {}
        def dfs(row, col):
            if row == 0 and col == 0:
                return 1
            if row < 0 or col < 0:
                return 0

            if (row-1, col) in paths:
                up = paths[(row-1,col)]
            else:
                up = dfs(row-1, col)
            if (row, col-1) in paths:
                left = paths[(row, col-1)]
            else:
                left = dfs(row, col-1)
            paths[(row, col)] = up + left
            return up + left
        return dfs(n-1, m-1)
