class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        START, END = 0, 1


        for elem in intervals:
            if elem[END] < newInterval[START]:
                result.append(elem)
            elif elem[START] > newInterval[END]:
                result.append(newInterval)
                newInterval = elem
            elif elem[START] <= newInterval[START] or elem[END] >= newInterval[END]:
                newInterval = [min(elem[START], newInterval[START]),
                               max(elem[END], newInterval[END])]
        result.append(newInterval)
        return result


if __name__ == '__main__':
    task = Solution()
    print(task.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))
