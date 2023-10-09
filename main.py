class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        result = 10 ** 7
        prev_pointer = 0
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            while curr_sum >= target:
                curr_sum -= nums[prev_pointer]
                result = min(result, i + 1 - prev_pointer)
                prev_pointer += 1

        return result if result != 10 ** 7 else 0


target = 7
nums = [2,3,1,2,4,3]

if __name__ == '__main__':
    task = Solution()
    print(task.minSubArrayLen(target, nums))
