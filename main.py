class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i, j = 0, 0
        while i < len(t):
            if t[i] == s[j]:
                j += 1
                if j == len(s):
                    return True
            i += 1
        return False


s = "abc"
t = "ahbgdc"

if __name__ == '__main__':
    task = Solution()
    print(task.isSubsequence(s, t))
