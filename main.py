class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, l = len(s1), len(s2), len(s3)

        if n + m != l:
            return False

        cache = [[False] * (m + 1) for _ in range(n + 1)]
        cache[0][0] = True

        for j in range(1, m + 1):
            cache[0][j] = cache[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, n + 1):
            cache[i][0] = cache[i - 1][0] and s1[i - 1] == s3[i - 1]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                cache[i][j] = (cache[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                              (cache[i][j - 1] and s2[j - 1] == s3[i + j - 1])

        return cache[n][m]


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

if __name__ == '__main__':
    task = Solution()
    print(task.isInterleave(s1, s2, s3))
