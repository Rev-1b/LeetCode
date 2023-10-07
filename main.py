class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            temp_sum = numbers[i] + numbers[j]
            if temp_sum == target:
                return [i + 1, j + 1]
            if temp_sum > target:
                j -= 1
            else:
                i += 1


numbers = [2, 7, 11, 15]
target = 9

if __name__ == '__main__':
    task = Solution()
    print(task.twoSum(numbers, target))
