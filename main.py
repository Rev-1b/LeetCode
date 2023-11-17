from random import randint


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        while True:
            temp_pivot = randint(left, right)
            pivot_index = self.do_magic(nums, left, right, temp_pivot)
            if len(nums) - k == pivot_index:
                return nums[pivot_index]
            if len(nums) - k > pivot_index:
                left = pivot_index + 1
            else:
                right = pivot_index - 1

    def do_magic(self, nums, left, right, pivot):
        pivot_num = nums[pivot]
        nums[pivot], nums[right] = nums[right], nums[pivot]
        far_left_pos = left
        for i in range(left, right):
            if nums[i] < pivot_num:
                nums[i], nums[far_left_pos] = nums[far_left_pos], nums[i]
                far_left_pos += 1
        nums[far_left_pos], nums[right] = nums[right], nums[far_left_pos]
        return far_left_pos


if __name__ == '__main__':
    task = Solution()

    nums = [3, 2, 1, 5, 6, 4]

    print(task.findKthLargest(nums, 2))
