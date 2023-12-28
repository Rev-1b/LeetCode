class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        result = [intervals[0]]
        i = 1

        while i < len(intervals):
            if result[-1][1] <= intervals[i][1]:
                if intervals[i][0] <= result[-1][1]:
                    result[-1][1] = intervals[i][1]
                else:
                    result.append(intervals[i])
            i += 1

        return result

if __name__ == '__main__':
    task = Solution()
    print(task.merge(intervals=[[1, 4], [2, 3]]))
