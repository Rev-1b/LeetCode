from collections import deque


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        n = len(board)
        m = len(board[0])
        
        def do_magic(deq: deque) -> None:
            while deq:
                elem_i, elem_j = deq.popleft()

                if 0 < elem_i and board[elem_i - 1][elem_j] == 'O':
                    board[elem_i - 1][elem_j] = 'S'
                    deq.append((elem_i - 1, elem_j))

                if n- 1 > elem_i and board[elem_i + 1][elem_j] == 'O':
                    board[elem_i + 1][elem_j] = 'S'
                    deq.append((elem_i + 1, elem_j))

                if 0 < elem_j and board[elem_i][elem_j - 1] == 'O':
                    board[elem_i][elem_j - 1] = 'S'
                    deq.append((elem_i, elem_j - 1))

                if m - 1 > elem_j and board[elem_i][elem_j + 1] == 'O':
                    board[elem_i][elem_j + 1] = 'S'
                    deq.append((elem_i, elem_j + 1))

        for j in range(m):
            if board[0][j] == 'O':
                board[0][j] = 'S'
                do_magic(deque(((0, j),)))

            if board[n- 1][j] == 'O':
                board[n- 1][j] = 'S'
                do_magic(deque(((n- 1, j),)))

        for i in range(n):
            if board[i][0] == 'O':
                board[i][0] = 'S'
                do_magic(deque(((i, 0),)))

            if board[i][m - 1] == 'O':
                board[i][m - 1] = 'S'
                do_magic(deque(((i, m - 1),)))

        for k in range(n):
            for q in range(m):
                if board[k][q] == 'S':
                    board[k][q] = 'O'

                elif board[k][q] == 'O':
                    board[k][q] = 'X'


if __name__ == '__main__':
    task = Solution()

    board = [["X", "X", "X", "X"],
             ["X", "O", "O", "X"],
             ["X", "X", "O", "X"],
             ["X", "O", "X", "X"]]

    task.solve(board)
    for w in board:
        print(*w)
