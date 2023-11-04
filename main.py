class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] <= nums[right]:
                return nums[left]
            mid = (left + right) // 2
            if nums[mid] < nums[left]:
                right = mid
            else:
                left = mid + 1


if __name__ == '__main__':
    task = Solution()

    nums = [3,1,2]

    print(task.findMin(nums))
