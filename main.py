from collections import deque
from itertools import chain


class Node:
    def __init__(self, val, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self):
        return f'Val="{self.val}"'


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:

        board.reverse()
        for i in range(1, len(board), 2):
            board[i].reverse()
        cells = [None] + list(chain(*board))

        stack = [1]
        visited = {1}
        n = len(board) ** 2
        steps = 0

        while stack:
            temp_stack = []
            for elem in stack:
                if elem == n:
                    return steps
                for curr in range(elem + 1, min(elem + 7, n + 1)):
                    curr = curr if cells[curr] == -1 else cells[curr]
                    if curr not in visited:
                        visited.add(curr)
                        temp_stack.append(curr)
            steps += 1
            stack = temp_stack

        return -1


if __name__ == '__main__':
    task = Solution()

    board = [[-1, -1, 19, 10, -1],
             [2, -1, -1, 6, -1],
             [-1, 17, -1, 19, -1],
             [25, -1, 20, -1, -1],
             [-1, -1, -1, -1, 15]]

    print(task.snakesAndLadders(board))
