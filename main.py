class Solution:
    def canJump(self, nums: list[int]) -> bool:
        target = nums[-1]

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= target:
                target = i

        if target == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    task = Solution()

    nums = [2, 3, 1, 1, 4]

    print(task.canJump(nums))
