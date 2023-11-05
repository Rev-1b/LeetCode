class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()
        i = 1
        while i <= len(citations):
            if citations[-i] < i:
                return i - 1
            i += 1
        return i - 1


if __name__ == '__main__':
    task = Solution()

    nums = [3, 2, 1, 5, 6, 4]


    print(task.hIndex(nums))
