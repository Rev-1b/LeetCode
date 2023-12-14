class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        for index, num in enumerate(citations, 1):
            if index > num:
                return index - 1
        return len(citations)


if __name__ == '__main__':
    task = Solution()
    print(task.hIndex([1,3,1]))
