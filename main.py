class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        rows, cols = set(), set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for k in rows:
            for l in range(m):
                matrix[k][l] = 0
        for q in cols:
            for w in range(n):
                matrix[w][q] = 0


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

if __name__ == '__main__':
    task = Solution()
    task.setZeroes(matrix)
    print(matrix)
