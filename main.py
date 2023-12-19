class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0

        storage = set(s[0])
        index = 0
        result = 1

        for i in range(1, len(s)):
            while s[i] in storage:
                storage.remove(s[index])
                index += 1
            storage.add(s[i])
            result = max(result, i + 1 - index)

        return result


if __name__ == '__main__':
    task = Solution()
    print(task.lengthOfLongestSubstring(s="abcabcbb"))
