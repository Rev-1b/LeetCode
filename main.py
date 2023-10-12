class Solution:
    def canConstruct(self, ransomNote, magazine):
        for i in set(ransomNote):
            if magazine.count(i) < ransomNote.count(i):
                return False
        return True


ransomNote = "aa"
magazine = "aab"

if __name__ == '__main__':
    task = Solution()
    print(task.canConstruct(ransomNote, magazine))
