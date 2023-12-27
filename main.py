class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(words) != len(pattern):
            return False

        pattern_dict, visited = {}, set()
        for char, word in zip(pattern, words):
            if char not in pattern_dict:
                if word in visited:
                    return False
                else:
                    pattern_dict[char] = word
                    visited.add(word)
            else:
                if pattern_dict[char] != word:
                    return False

        return True


if __name__ == '__main__':
    task = Solution()
    print(task.wordPattern(pattern="abba", s="dog cat cat dog"))
