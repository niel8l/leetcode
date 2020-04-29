from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                live = dead = 0
                for x, y in [
                    (i-1, j-1),
                    (i-1, j),
                    (i-1, j+1),
                    (i, j-1),
                    (i, j+1),
                    (i+1, j-1),
                    (i+1, j),
                    (i+1, j+1)
                ]:
                    if 0 <= x < m and 0 <= y < n:
                        if board[x][y] == 0 or board[x][y] == 2:
                            dead += 1
                        else:  # board[x][y] == 1 or board[x][y] == -1:
                            live += 1
                v = board[i][j]
                if v == 1:
                    # rule 1
                    if live < 2:
                        board[i][j] = -1
                    elif live > 3:
                        # rule 3
                        board[i][j] = -1
                # rule 4
                elif live == 3:
                    board[i][j] = 2
        for i in range(m):
            for j in range(n):
                v = board[i][j]
                if v == 2:
                    board[i][j] = 1
                elif v == -1:
                    board[i][j] = 0


s = Solution()
board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]
s.gameOfLife(board)
print(board)
