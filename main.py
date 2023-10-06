class Solution:
    def isPalindrome(self, string: str) -> bool:
        string = "".join(c for c in string.lower() if c.isalnum())
        return string == string[::-1]


s = "A man, a plan, a canal: Panama"

if __name__ == '__main__':
    task = Solution()
    print(task.isPalindrome(s))
