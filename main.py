class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = float('-inf')
        curr_sum = 0

        for num in nums:
            curr_sum += num

            if curr_sum > max_sum:
                max_sum = curr_sum

            if curr_sum < 0:
                curr_sum = 0

        return max_sum


if __name__ == '__main__':
    task = Solution()

    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    print(task.maxSubArray(nums1))
