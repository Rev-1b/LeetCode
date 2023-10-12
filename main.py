from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


s = "anagram"
t = "nagaram"

if __name__ == '__main__':
    task = Solution()
    print(task.isAnagram(s, t))
