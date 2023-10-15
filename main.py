class Solution:
    def isValid(self, s: str) -> bool:
        closed = {')': '(', ']': '[', '}': '{'}
        stack = ''

        for char in s:
            if char in closed:
                if stack and closed[char] == stack[-1]:
                    stack = stack[:-1]
                else:
                    return False
            else:
                stack += char
        return not stack


s = "()[]{}(}"

if __name__ == '__main__':
    task = Solution()
    print(task.isValid(s))

