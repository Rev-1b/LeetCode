class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        cache = {}

        for index, num in enumerate(nums):
            aim = target - num
            if aim in cache:
                return cache[aim], index
            else:
                cache[num] = index


if __name__ == '__main__':
    task = Solution()
    print(task.twoSum(nums=[2, 7, 11, 15], target=9))
