class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            if result[-1][1] <= intervals[i][1]:
                if intervals[i][0] <= result[-1][1]:
                    result[-1][1] = intervals[i][1]
                else:
                    result.append(intervals[i])

        return result


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

if __name__ == '__main__':
    task = Solution()
    print(task.merge(intervals))
