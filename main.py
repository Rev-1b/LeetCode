from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def do_magic(deq: deque) -> None:
            while deq:
                elem_i, elem_j = deq.popleft()

                if 0 < elem_i and grid[elem_i - 1][elem_j] == '1':
                    grid[elem_i - 1][elem_j] = '0'
                    deq.append((elem_i - 1, elem_j))

                if len(grid) - 1 > elem_i and grid[elem_i + 1][elem_j] == '1':
                    grid[elem_i + 1][elem_j] = '0'
                    deq.append((elem_i + 1, elem_j))

                if 0 < elem_j and grid[elem_i][elem_j - 1] == '1':
                    grid[elem_i][elem_j - 1] = '0'
                    deq.append((elem_i, elem_j - 1))

                if len(grid[0]) - 1 > elem_j and grid[elem_i][elem_j + 1] == '1':
                    grid[elem_i][elem_j + 1] = '0'
                    deq.append((elem_i, elem_j + 1))

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    islands += 1
                    do_magic(deque(((i, j),)))

        return islands


if __name__ == '__main__':
    task = Solution()

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    print(task.numIslands(grid))
