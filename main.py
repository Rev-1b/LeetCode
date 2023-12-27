class Solution:
    def canConstruct(self, ransomNote, magazine):
        for i in set(ransomNote):
            if magazine.count(i) < ransomNote.count(i):
                return False
        return True


if __name__ == '__main__':
    task = Solution()
    print(task.canConstruct(ransomNote="aa", magazine="aab"))
