class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left = 0

        for i in range(2, len(nums)):
            if nums[i] != nums[left]:
                nums[left + 2] = nums[i]
                left += 1
        return left + 2


if __name__ == '__main__':
    task = Solution()
    print(task.removeDuplicates(nums=[0, 0, 1, 1, 1, 1, 2, 3, 3]))
