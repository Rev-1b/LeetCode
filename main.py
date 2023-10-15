class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        temp_storage = []
        temp = ''
        for char in path:
            if char == '/':
                if temp:
                    temp_storage.append(temp)
                    temp = ''
            else:
                temp += char
        if temp:
            temp_storage.append(temp)

        for elem in temp_storage:
            if elem == '..':
                stack = stack[:-1]
            elif elem != '.':
                stack.append(elem)
        return f'/{"/".join(stack)}'


path = "/../"

if __name__ == '__main__':
    task = Solution()
    print(task.simplifyPath(path))

