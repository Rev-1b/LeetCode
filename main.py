class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        matrix.reverse()

        for i in range(1, len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]



matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

if __name__ == '__main__':
    task = Solution()
    print(task.rotate(matrix=matrix))
    for row in matrix:
        print(*row)
