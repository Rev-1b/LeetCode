class Solution:
    def canJump(self, nums: list[int]) -> bool:
        jump = nums[0]

        for num in nums[1:]:
            if not jump:
                return False
            jump = max(jump - 1, num)
        return True


if __name__ == '__main__':
    task = Solution()
    print(task.canJump(nums=[3, 2, 1, 0, 4]))
