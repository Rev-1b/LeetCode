class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for j in range(len(nums) - 1, -1, -1):
            answer[j] *= postfix
            postfix *= nums[j]

        return answer


if __name__ == '__main__':
    task = Solution()

    nums = [3, 2, 1, 5, 6, 4]

    print(task.productExceptSelf(nums))
