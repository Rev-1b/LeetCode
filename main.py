class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 1
        last = 0
        our_set = set(s[0])

        for i in range(1, len(s)):
            while s[i] in our_set:
                our_set.remove(s[last])
                last += 1
            our_set.add(s[i])
            result = max(result, i + 1 - last)

        return result


s = "pwwkew"
if __name__ == '__main__':
    task = Solution()
    print(task.lengthOfLongestSubstring(s))
