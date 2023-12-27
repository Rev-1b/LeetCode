class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_main, t_main = {}, {}
        for s_char, t_char in zip(s, t):
            s_temp = s_main.setdefault(s_char, t_char)
            t_temp = t_main.setdefault(t_char, s_char)
            if s_temp != t_char or t_temp != s_char:
                return False
        return True


if __name__ == '__main__':
    task = Solution()
    print(task.isIsomorphic(s="bads", t="baba"))
