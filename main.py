class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        n, m = len(board), len(board[0])

        for i in range(n):
            for j in range(m):
                temp_counter = 0
                i_start = i - 1 if i > 1 else 0
                i_end = i + 2 if i < n - 2 else n
                j_start = j - 1 if j > 1 else 0
                j_end = j + 2 if j < m - 2 else m

                for i1 in range(i_start, i_end):
                    for j1 in range(j_start, j_end):
                        if i1 == i and j1 == j:
                            continue
                        if board[i1][j1] == 'dead' or board[i1][j1] == 1:
                            temp_counter += 1

                if board[i][j]:
                    if temp_counter < 2 or temp_counter > 3:
                        board[i][j] = 'dead'
                else:
                    if temp_counter == 3:
                        board[i][j] = 'alive'
        for k in range(n):
            for q in range(m):
                if board[k][q] == 'alive':
                    board[k][q] = 1
                elif board[k][q] == 'dead':
                    board[k][q] = 0


board = [[0, 1, 0],
         [0, 0, 1],
         [1, 1, 1],
         [0, 0, 0]]

if __name__ == '__main__':
    task = Solution()
    task.gameOfLife(board)
    print(board)
