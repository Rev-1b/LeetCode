class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        cache = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for j in range(1, m + 1):
            cache[0][j] = j

        for i in range(1, n + 1):
            cache[i][0] = i

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    cache[i][j] = cache[i - 1][j - 1]

                else:
                    cache[i][j] = 1 + min(cache[i - 1][j - 1],
                                          cache[i][j - 1],
                                          cache[i - 1][j])

        return cache[n][m]


word1 = "рупор"
word2 = "р"

if __name__ == '__main__':
    task = Solution()
    print(task.minDistance(word1, word2))
