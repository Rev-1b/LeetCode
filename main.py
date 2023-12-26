class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = [matrix[0][0]]
        step = 0
        direction = 0
        i, j = 0, 0
        n, m = len(matrix), len(matrix[0])

        while len(result) < n * m:
            if direction == 0:
                if j + step < m - 1:
                    j += 1
                else:
                    direction += 1
                    continue
            elif direction == 1:
                if i + step < n - 1:
                    i += 1
                else:
                    direction += 1
                    continue
            elif direction == 2:
                if j > step:
                    j -= 1
                else:
                    direction += 1
                    continue
            elif direction == 3:
                if i >= step + 2:
                    i -= 1
                else:
                    direction = 0
                    step += 1
                    continue

            result.append(matrix[i][j])

        return result


if __name__ == '__main__':
    task = Solution()
    print(task.spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
