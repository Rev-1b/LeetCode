class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        n, m = len(matrix), len(matrix[0])

        if all(i == '0' for row in matrix for i in row):
            return 0

        result = 1

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == '1':
                    a, b, c = map(int, (matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i][j - 1]))
                    if a and b and c:
                        res = min(a, b, c) + 1
                        matrix[i][j] = str(res)
                        result = max(res, result)

        return result ** 2


matrix = [["1", "1", "1", "1", "0"],
          ["1", "1", "1", "1", "0"],
          ["1", "1", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["0", "0", "1", "1", "1"]]

if __name__ == '__main__':
    task = Solution()
    print(task.maximalSquare(matrix))
