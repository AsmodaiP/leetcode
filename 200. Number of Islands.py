# https://leetcode.com/problems/number-of-islands
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        max_row, max_col = len(grid), len(grid[0])

        def delete_island(x, y):
            if 0 <= x < max_row and 0 <= y < max_col and grid[x][y] == '1':
                grid[x][y] = '0'
                for neighbor_x, neighbor_y in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    delete_island(neighbor_x, neighbor_y)

        island_count = 0

        for row in range(max_row):
            for column in range(max_col):
                if grid[row][column] == '1':
                    island_count += 1
                    delete_island(row, column)
        return island_count
