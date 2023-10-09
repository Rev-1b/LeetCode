class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = {}
        left = 0
        result = 0

        for i in range(len(s)):
            if s[i] not in seen_chars:
                result = max(result, i + 1 - left)
            else:
                while seen_chars[s[i]] >= left:
                    left += 1
                result = max(result, i + 1 - left)
            seen_chars[s[i]] = i

        return result


s = "pwwkew"

if __name__ == '__main__':
    task = Solution()
    print(task.lengthOfLongestSubstring(s))
