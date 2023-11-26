class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        cache: list[int] = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            cache.append(max(cache[i - 1], cache[i - 2] + nums[i]))
        return cache[-1]


nums = [2, 7, 9, 3, 1]

if __name__ == '__main__':
    task = Solution()
    print(task.rob(nums))
