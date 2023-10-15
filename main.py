class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '/': lambda x, y: int(x / y),
            '*': lambda x, y: x * y,
        }

        for elem in tokens:
            if elem in operators:
                y = stack.pop()
                x = stack.pop()
                func = operators[elem]
                stack.append(func(x, y))
            else:
                stack.append(int(elem))
        return stack[0]


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]


if __name__ == '__main__':
    task = Solution()
    print(task.evalRPN(tokens))
