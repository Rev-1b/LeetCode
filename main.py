class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        up, down = 0, len(matrix) - 1

        row = None
        while up <= down:
            mid = (up + down) // 2
            if matrix[mid][0] > target:
                down = mid - 1
            elif matrix[mid][-1] < target:
                up = mid + 1
            else:
                row = matrix[mid]
                break

        if row is None:
            return False

        start, end = 0, len(row) - 1
        while start <= end:
            mid = (start + end) // 2
            if row[mid] == target:
                return True
            if row[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return False


if __name__ == '__main__':
    task = Solution()

    matrix = [[1,  3,  5,  7],
              [10, 11, 16, 20],
              [23, 30, 34, 60]]

    target = 0

    print(task.searchMatrix(matrix, target))
