class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:

        curr_sum = 0

        local_min_sum, global_min_sum = 0, float('inf')
        local_max_sum, global_max_sum = 0, float('-inf')

        for number in nums:
            local_min_sum = min(local_min_sum + number, number)
            global_min_sum = min(global_min_sum, local_min_sum)

            local_max_sum = max(local_max_sum + number, number)
            global_max_sum = max(global_max_sum, local_max_sum)

            curr_sum += number

        if global_max_sum > 0:
            return max(curr_sum - global_min_sum, global_max_sum)
        else:
            return global_max_sum


if __name__ == '__main__':
    task = Solution()

    nums1 = [5, -3, 5]
    print(task.maxSubarraySumCircular(nums1))
