from collections import deque, defaultdict
from typing import Optional


class Node:
    def __init__(self, val, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        self.visited = False

    def __str__(self):
        return f'Val="{self.val}"'


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        storage = [[] for _ in range(numCourses)]
        income_links = [0] * numCourses
        for end, start in prerequisites:
            storage[start].append(end)
            income_links[end] += 1

        queue = deque(i for (i, d) in enumerate(income_links) if d == 0)

        visited = 0
        while queue:
            node = queue.popleft()
            visited += 1
            for curr in storage[node]:
                income_links[curr] -= 1
                if not income_links[curr]:
                    queue.append(curr)

        return visited == numCourses


if __name__ == '__main__':
    task = Solution()

    numCourses = 2
    prerequisites = [[1, 0]]

    print(task.canFinish(numCourses, prerequisites))
