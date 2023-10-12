class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_set = {}

        for index, num in enumerate(nums):
            if target - num in nums_set:
                return nums_set[target - num], index
            nums_set[num] = index


nums = [3, 2, 4]
target = 6

if __name__ == '__main__':
    task = Solution()
    print(task.twoSum(nums, target))
