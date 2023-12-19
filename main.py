class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        result = float('inf')
        curr_sum, index = 0, 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            while curr_sum >= target:
                curr_sum -= nums[index]
                result = min(result, i + 1 - index)
                index += 1

        return result if result != float('-inf') else 0



if __name__ == '__main__':
    task = Solution()
    print(task.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
