class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()
        while n != 1:
            if n in cache:
                return False
            cache.add(n)
            temp = 0
            for digit in str(n):
                temp += int(digit) ** 2
            n = temp

        return True



if __name__ == '__main__':
    task = Solution()
    print(task.isHappy(n=19))
