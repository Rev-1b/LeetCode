class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: list[list[int]]) -> Node:
        n = len(grid)
        amount = sum(grid[i][j] for i in range(n) for j in range(n))
        if amount == n ** 2:
            return Node(True, True, None, None, None, None)
        if not amount:
            return Node(False, True, None, None, None, None)

        top = grid[:n // 2]
        bottom = grid[n // 2:]
        top_left = self.construct([row[:n // 2] for row in top])
        top_right = self.construct([row[n // 2:] for row in top])
        bottom_left = self.construct([row[:n // 2] for row in bottom])
        bottom_right = self.construct([row[n // 2:] for row in bottom])
        return Node(True, False, top_left, top_right, bottom_left, bottom_right)


if __name__ == '__main__':
    task = Solution()

    grid1 = [[1, 1, 1, 1, 0, 0, 0, 0],
             [1, 1, 1, 1, 0, 0, 0, 0],
             [1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 0, 0, 0, 0],
             [1, 1, 1, 1, 0, 0, 0, 0],
             [1, 1, 1, 1, 0, 0, 0, 0],
             [1, 1, 1, 1, 0, 0, 0, 0]]

    print(task.construct(grid1))
