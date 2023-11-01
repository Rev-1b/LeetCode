from collections import Counter


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        rows = len(board)
        columns = len(board[0])

        if len(word) > rows * columns:
            return False

        count = Counter(sum(board, []))

        for char, char_number in Counter(word).items():
            if count[char] < char_number:
                return False

        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        visited = set()

        def do_magic(row, col, i):
            if i == len(word):
                return True

            if not 0 <= row < rows or not 0 <= col < columns or word[i] != board[row][col] or (row, col) in visited:
                return False

            visited.add((row, col))
            res = (
                    do_magic(row + 1, col, i + 1) or
                    do_magic(row - 1, col, i + 1) or
                    do_magic(row, col + 1, i + 1) or
                    do_magic(row, col - 1, i + 1)
            )
            visited.remove((row, col))

            return res

        for i in range(rows):
            for j in range(columns):
                if do_magic(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    task = Solution()

    board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word1 = "ABCCED"

    print(task.exist(board1, word1))
