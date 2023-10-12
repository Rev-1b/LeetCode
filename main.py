class Solution:
    def isHappy(self, n: int) -> bool:
        prev_nums = {n}
        while n != 1:
            temp = 0
            for digit in str(n):
                temp += int(digit) ** 2
            if temp in prev_nums:
                return False
            prev_nums.add(temp)
            n = temp
        return True


n = 19

if __name__ == '__main__':
    task = Solution()
    print(task.isHappy(n))
