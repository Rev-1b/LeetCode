class Solution:
    def candy(self, ratings: list[int]) -> int:
        pchely = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                pchely[i] = pchely[i - 1] + 1
        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j + 1] and pchely[j] <= pchely[j + 1]:
                pchely[j] = pchely[j + 1] + 1
        return sum(pchely)


ratings = [1, 2, 2]

if __name__ == '__main__':
    task = Solution()
    print(task.candy(ratings))
