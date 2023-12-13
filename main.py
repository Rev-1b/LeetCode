class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        prev = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[prev]:
                nums[prev + 1] = nums[i]
                prev += 1
        return prev + 1


if __name__ == '__main__':
    task = Solution()
    print(task.removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
