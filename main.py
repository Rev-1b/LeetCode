from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        tmp_res = defaultdict(list)

        for word in strs:
            count = ''.join(sorted(word))
            tmp_res[count].append(word)

        return tmp_res.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

if __name__ == '__main__':
    task = Solution()
    print(task.groupAnagrams(strs))
