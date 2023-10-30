class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []

        def backtrack(remain, comb, mod):
            if remain == 0:
                result.append(comb.copy())
            else:
                for i in range(mod, n + 1):
                    comb.append(i)
                    backtrack(remain - 1, comb, i + 1)
                    comb.pop()

        backtrack(k, [], 1)
        return result


if __name__ == '__main__':
    task = Solution()

    n, k = 6, 3

    print(task.combine(n, k))
