class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:

        start_i, start_j = 1, 0
        n, m = len(grid), len(grid[0])

        if n == 1:
            return sum(grid[0])

        while True:
            i, j = start_i, start_j

            while j < m and i >= 0:
                left = grid[i][j - 1] if j > 0 else 1000
                top = grid[i - 1][j] if i > 0 else 1000

                grid[i][j] += min(left, top)

                if i == n - 1 and j == m - 1:
                    return grid[i][j]

                i -= 1
                j += 1

            if start_i < n - 1:
                start_i += 1
            else:
                start_j += 1


grid = [[0]]

if __name__ == '__main__':
    task = Solution()
    print(task.minPathSum(grid))
