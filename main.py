class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        while n:
            counter += n & 1
            n >>= 1
        return counter


n = 0b11111111111111111111111111111101

if __name__ == '__main__':
    task = Solution()
    print(task.hammingWeight(n))
