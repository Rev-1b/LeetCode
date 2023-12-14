class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        slow = prices[0]
        res = 0

        for num in prices[1:]:
            if slow < num:
                res += num - slow
            slow = num

        return res


if __name__ == '__main__':
    task = Solution()
    print(task.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
