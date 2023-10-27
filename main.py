from collections import deque


class Node:
    def __init__(self, val, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        self.visited = False

    def __str__(self):
        return f'Val="{self.val}"'


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        outgoing = [[] for _ in range(numCourses)]
        incoming = [0] * numCourses

        for end, start in prerequisites:
            outgoing[start].append(end)
            incoming[end] += 1

        queue = deque(i for i, d in enumerate(incoming) if not d)
        right_order = []
        while queue:
            curr = queue.popleft()
            right_order.append(curr)
            for child in outgoing[curr]:
                incoming[child] -= 1
                if not incoming[child]:
                    queue.append(child)

        return right_order if len(right_order) == numCourses else []


if __name__ == '__main__':
    task = Solution()

    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [1, 3]]

    print(task.canFinish(numCourses, prerequisites))
