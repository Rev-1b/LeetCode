class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        n //= 5

        while n:
            result += n
            n //= 5

        return result


n = 120
if __name__ == '__main__':
    task = Solution()
    print(task.trailingZeroes(n))
