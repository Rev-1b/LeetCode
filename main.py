class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == haystack:
            return needle

        i, j = 0, len(needle)

        while j <= len(haystack):
            if haystack[i:j] == needle:
                return i

            i += 1
            j += 1

        return -1


if __name__ == '__main__':
    task = Solution()
    print(task.strStr(haystack="sadbutsad", needle="sd"))
