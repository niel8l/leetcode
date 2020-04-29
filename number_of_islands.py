from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        if not grid:
            return count
        nr = len(grid)
        nc = len(grid[0])
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)
        return count

    def dfs(self, grid, i, j):
        nr = len(grid)
        nc = len(grid[0])
        if i < 0 or j < 0 or i >= nr or j >= nc or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid, i-1, j)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i, j+1)


s = Solution()
print(s.numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))  # NOQA
