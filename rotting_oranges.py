
"""
1. 初始化 queue
2. 遍历 grid, 统计新鲜橙子的数量, 腐烂橙子的坐标添加到 queue
3. 添加 (-1, -1) 到 queue 中, 作为每分钟污染的结束标识
4. 当 queue 不是空时:
    4.1 检查 queue 的第一个元素的坐标是不是 -1, 如果是 -1,表示该分钟污染结束, 从 queue 中删除第一个元素, 分钟数加 1; 如果 queue 不为空, 下一分钟仍然需要污染, 添加 (-1, -1) 到 queue 末尾, 作为下一分钟污染的结束标识
    4.2 如果 4.1 中的第一个元素坐标不是 -1, 则需要从四个方向污染新鲜橙子: 将污染的橙子改成 2, 添加该坐标到 queue, 作为下一次污染的根, 新鲜橙子数量 -1.
5. 返回新鲜橙子数量, 如果没有新鲜橙子, 返回-1.
"""  # NOQA


from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        queue = deque()
        nr = len(grid)
        nc = len(grid[0])
        minutes = fresh = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        queue.append((-1, -1))
        while queue:
            i, j = queue.popleft()
            if i == -1:
                if queue:
                    minutes += 1
                    queue.append((-1, -1))
            else:
                for x, y in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    ni, nj = i + x, j + y
                    if nr > ni >= 0 and nc > nj >= 0 and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        queue.append((ni, nj))
        return minutes if fresh == 0 else -1


s = Solution()
print(s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
