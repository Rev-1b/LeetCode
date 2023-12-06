class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        i = 1

        while i < len(triangle):
            row = triangle[i]
            j = 0

            while j < len(row):
                if j == 0:
                    triangle[i][j] = triangle[i - 1][0] + triangle[i][j]

                elif j == len(row) - 1:
                    triangle[i][j] = triangle[i - 1][len(row) - 2] + triangle[i][j]

                else:
                    triangle[i][j] = min(triangle[i - 1][j] + triangle[i][j],
                                         triangle[i - 1][j - 1] + triangle[i][j])

                j += 1
            i += 1

        return min(triangle[-1])


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]

if __name__ == '__main__':
    task = Solution()
    print(task.minimumTotal(triangle))
