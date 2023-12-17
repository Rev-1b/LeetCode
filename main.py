class Solution:
    def convert(self, s: str, numb: int) -> str:
        if numb == 1:
            return s

        storage = ['' for _ in range(numb)]

        pointer = 0
        mult = 1
        for char in s:
            storage[pointer] += char

            if pointer == numb - 1:
                mult = -1

            if pointer == 0:
                mult = 1

            pointer += mult

        return ''.join(storage)


if __name__ == '__main__':
    task = Solution()
    print(task.convert(s="PAYPALISHIRING", numb=3))
