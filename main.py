from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        all_chars = defaultdict(list)
        for i in range(9):
            for j in range(9):
                char = board[i][j]
                if char.isdigit():
                    square_pos = (i // 3, j // 3)
                    for pre_val in all_chars[char]:
                        if i == pre_val[0][0] or j == pre_val[0][1] or square_pos == pre_val[1]:
                            return False
                    all_chars[char].append(((i, j), square_pos))
        return True


board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

if __name__ == '__main__':
    task = Solution()
    print(task.isValidSudoku(board))
