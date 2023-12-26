class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        n, m = len(board), len(board[0])

        for i in range(n):
            for j in range(m):
                living_cells = 0

                i_start = i - 1 if i > 1 else 0
                j_start = j - 1 if j > 1 else 0
                i_end = i + 2 if i < n - 1 else n
                j_end = j + 2 if j < m - 1 else m

                for k in range(i_start, i_end):
                    for q in range(j_start, j_end):
                        if not (k == i and q == j) and board[k][q] in (1, 'D'):
                            living_cells += 1

                if board[i][j] == 1 and not 2 <= living_cells <= 3:
                    board[i][j] = 'D'
                if board[i][j] == 0 and living_cells == 3:
                    board[i][j] = 'A'

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'D':
                    board[i][j] = 0
                if board[i][j] == 'A':
                    board[i][j] = 1

        return board


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]

if __name__ == '__main__':
    task = Solution()
    print(task.gameOfLife(board))
