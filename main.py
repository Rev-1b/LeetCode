class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))


if __name__ == '__main__':
    task = Solution()
    print(task.reverseWords(s=" the sky is blue "))
