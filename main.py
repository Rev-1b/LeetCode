class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        result = []
        i = 0

        while i < len(nums):
            left = right = i
            while right + 1 < len(nums) and nums[right] + 1 == nums[right + 1]:
                right += 1
            if left == right:
                result.append(f'{nums[left]}')
            else:
                result.append(f'{nums[left]}->{nums[right]}')
            i = right + 1

        return result



if __name__ == '__main__':
    task = Solution()
    print(task.summaryRanges(nums=[0, 1, 2, 4, 5, 7]))

    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(sorted(nums))
