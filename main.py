class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        temp = ''
        result = []

        for char in path:
            if char == '/':
                if temp:
                    stack.append(temp)
                    temp = ''
            else:
                temp += char
        if temp:
            stack.append(temp)

        for elem in stack:
            if elem == '..':
                if result:
                    result = result[:-1]
            elif elem != '.':
                result.append(elem)

        return '/' + '/'.join(result)


if __name__ == '__main__':
    task = Solution()
    print(task.simplifyPath(path="/home//foo/"))
