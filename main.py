from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> str:

        cache = defaultdict(list)
        longest_palindrome = s[0]

        def is_palindrome(word):
            if len(word) in [0, 1]:
                return True

            if word[0] != word[-1]:
                return False

            else:
                return is_palindrome(word[1:-1])

        for index, char in enumerate(s):
            if cache[char]:
                lst = cache[char]
                for i in lst:
                    if len(longest_palindrome) <= index - i:
                        res = is_palindrome(s[i:index + 1])
                        if res:
                            longest_palindrome = s[i:index + 1]
                            break
                    else:
                        break

            cache[char].append(index)

        return longest_palindrome


s = "aacabdkacaa"

if __name__ == '__main__':
    task = Solution()
    print(task.longestPalindrome(s))
