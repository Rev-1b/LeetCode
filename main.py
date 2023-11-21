class Solution:
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            if n & 1:
                res += 1 << (31 - i)
            n >>= 1
        return res


n = 11111111111111111111111111111101

if __name__ == '__main__':
    task = Solution()
    print(task.reverseBits(n))
