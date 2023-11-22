class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        i = len(digits) - 1
        rest = 1

        while digits[i] + rest == 10:
            digits[i] = 0
            i -= 1

        if i == -1:
            digits.insert(0, 1)
        else:
            digits[i] = digits[i] + 1

        return digits


digits = [9, 8, 9, 9, 9]

if __name__ == '__main__':
    task = Solution()
    print(task.plusOne(digits))
