class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        start_i, start_j = 1, 0
        n, m = len(obstacleGrid), len(obstacleGrid[0])

        if n == 1 and m == 1:
            return 1

        if n == 1:
            temp = sum(obstacleGrid[0])
            return 1 if temp == 0 else 5

        obstacleGrid[0][0] = 1

        while True:
            i, j = start_i, start_j

            while j < m and i >= 0:
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = None
                else:
                    left = obstacleGrid[i][j - 1] if j > 0 and obstacleGrid[i][j - 1] is not None else 0
                    top = obstacleGrid[i - 1][j] if i > 0 and obstacleGrid[i - 1][j] is not None else 0

                    obstacleGrid[i][j] = left + top

                if i == n - 1 and j == m - 1:
                    return obstacleGrid[i][j]

                i -= 1
                j += 1

            if start_i < n - 1:
                start_i += 1
            else:
                start_j += 1


obstacleGrid = [[0, 0]]

if __name__ == '__main__':
    task = Solution()
    print(task.uniquePathsWithObstacles(obstacleGrid))
