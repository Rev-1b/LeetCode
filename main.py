class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        stage = 0
        direction = 0
        i, j = 0, 0
        n, m = len(matrix), len(matrix[0])
        result = [matrix[0][0]]
        while True:
            if len(result) == n * m:
                return result
            if not direction:
                if j + 1 + stage < m:
                    j += 1
                else:
                    direction += 1
                    continue
            elif direction == 1:
                if i + 1 + stage < n:
                    i += 1
                else:
                    direction += 1
                    continue
            elif direction == 2:
                if j - 1 - stage >= 0:
                    j -= 1
                else:
                    direction += 1
                    continue
            else:
                if i - 1 - stage >= 1:
                    i -= 1
                else:
                    direction = 0
                    stage += 1
                    continue
            result.append(matrix[i][j])


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

if __name__ == '__main__':
    task = Solution()
    print(task.spiralOrder(matrix))
