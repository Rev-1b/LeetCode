class Solution:
    def addBinary(self, a: str, b: str) -> str:
        additional = 0
        a_pointer, b_pointer = len(a) - 1, len(b) - 1

        res = ''
        while a_pointer >= 0 or b_pointer >= 0 or additional:
            if a_pointer >= 0:
                additional += int(a[a_pointer])

            if b_pointer >= 0:
                additional += int(b[b_pointer])

            res = str(additional % 2) + res
            additional //= 2

            a_pointer -= 1
            b_pointer -= 1

        return res





a = "1010"
b = "1011"

if __name__ == '__main__':
    task = Solution()
    print(task.addBinary(a, b))
