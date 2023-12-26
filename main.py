from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        cache = defaultdict(list)

        for i in range(9):
            for j in range(9):
                elem = board[i][j]
                if elem.isdigit():
                    group = (i // 3, j // 3)
                    if elem in cache:
                        for coords in cache[elem]:
                            i1, j1 = coords
                            if i1 == i or j1 == j or (i1 // 3, j1 // 3) == group:
                                return False
                    cache[elem].append((i, j))

        return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         ["3", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

if __name__ == '__main__':
    task = Solution()
    print(task.isValidSudoku(board))
