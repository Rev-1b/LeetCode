class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]

if __name__ == '__main__':
    task = Solution()
    print(task.rotate(matrix))
