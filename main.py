class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


if __name__ == '__main__':
    task = Solution()
    print(task.majorityElement(nums=[2, 2, 1, 1, 1, 2, 2]))
