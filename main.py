class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        if nums[mid] > target:
            return mid
        return mid + 1


if __name__ == '__main__':
    task = Solution()

    nums = [1, 3, 5, 6, 8, 13, 19]
    target = 18

    print(task.searchInsert(nums, target))
