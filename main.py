class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1 for _ in range(len(nums))]

        prefix = 1
        for i in range(len(nums)):
            result[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for j in range(len(nums) - 1, -1, -1):
            result[j] *= postfix
            postfix *= nums[j]

        return result


if __name__ == '__main__':
    task = Solution()
    print(task.productExceptSelf(nums=[1, 2, 3, 4, 5]))
