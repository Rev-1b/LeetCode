class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows, cols = set(), set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for row in rows:
            matrix[row] = [0] * len(matrix[0])

        for col in cols:
            for i in range(len(matrix)):
                matrix[i][col] = 0


matrix = [[1, 1, 1],
          [1, 0, 1],
          [1, 1, 1]]

if __name__ == '__main__':
    task = Solution()
    print(task.setZeroes(matrix=matrix))
    for row in matrix:
        print(*row)
