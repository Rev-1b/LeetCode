class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[left] = nums[i]
                left += 1

        return left


if __name__ == '__main__':
    task = Solution()
    print(task.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))
