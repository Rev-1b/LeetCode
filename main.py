class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_lst = s.split()
        if len(pattern) != len(s_lst):
            return False
        pattern_map, heap = {}, set()
        for char, word in zip(pattern, s_lst):
            if char not in pattern_map and word in heap:
                return False
            tmp_res = pattern_map.setdefault(char, word)
            if tmp_res != word:
                return False
            heap.add(word)
        return True


pattern = "abba"
s = "dog dog dog dog"

if __name__ == '__main__':
    task = Solution()
    print(task.wordPattern(pattern, s))
