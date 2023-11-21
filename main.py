class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0

        for num in nums:
            result ^= num

        return result


nums = [4, 1, 2, 1, 2]

if __name__ == '__main__':
    task = Solution()
    print(task.singleNumber(nums))
