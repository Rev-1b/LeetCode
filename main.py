class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        cache = [amount + 1] * (amount + 1)
        cache[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if coin <= i:
                    cache[i] = min(cache[i], cache[i - coin] + 1)
        return -1 if cache[amount] == amount + 1 else cache[amount]


coins = [1, 2, 5]
amount = 11

if __name__ == '__main__':
    task = Solution()
    print(task.coinChange(coins, amount))
