class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0

        slow = prices[0]
        for num in prices[1:]:
            if slow < num:
                res = max(res, num - slow)
            else:
                slow = num
        return res


if __name__ == '__main__':
    task = Solution()
    print(task.maxProfit(prices=[7, 6, 4, 3, 1]))
