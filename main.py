class Solution:
    def climbStairs(self, n: int) -> int:
        pre, cur = 0,1
        for i in range(n):
            pre, cur = cur, pre+cur
        return cur
n = 8

if __name__ == '__main__':
    task = Solution()
    print(task.climbStairs(n))
