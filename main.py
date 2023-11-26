class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        bad_words = set()

        def do_magic(string: str) -> bool:
            res = False
            if string in bad_words:
                return res

            if not string:
                return True

            for word in wordDict:
                if res:
                    return res
                if string.startswith(word):
                    res = do_magic(string[len(word):])

            bad_words.add(string)
            return res

        return do_magic(s)


s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

if __name__ == '__main__':
    task = Solution()
    print(task.wordBreak(s, wordDict))
