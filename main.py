class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        start, end = 0, len(nums) - 1

        if end == 1:
            return 0 if nums[start] > nums[end] else 1

        while start <= end:
            mid = (start + end) // 2

            if mid == 0 or mid == len(nums) - 1 or nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid

            if nums[mid] < nums[mid + 1]:
                start = mid + 1

            else:
                end = mid


if __name__ == '__main__':
    task = Solution()

    nums = [3, 4, 3, 2, 1]

    print(task.findPeakElement(nums))
