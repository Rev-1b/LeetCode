class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def do_magic(res: str, opening: int, closing: int) -> None:
            if not opening and closing == 1:
                result.append(f'{res})')
                return
            if opening:
                do_magic(f'{res}(', opening - 1, closing)
            if opening < closing:
                do_magic(f'{res})', opening, closing - 1)

        do_magic('', n, n)
        return result


if __name__ == '__main__':
    task = Solution()

    n = 1
    print(task.generateParenthesis(n))
