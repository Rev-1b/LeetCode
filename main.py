class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = {}
        left, result = 0, 0

        for i in range(len(s)):
            if s[i] in seen_chars:
                if seen_chars[s[i]] >= left:
                    left = seen_chars[s[i]] + 1
            result = max(result, i + 1 - left)
            seen_chars[s[i]] = i
        return result


s = " "

if __name__ == '__main__':
    task = Solution()
    print(task.lengthOfLongestSubstring(s))
