from collections import deque
from typing import Optional


class Node:
    def __init__(self, char, neighbors=None):
        self.char = char
        self.neighbors = neighbors if neighbors is not None else {}

    def __str__(self):
        return f'Char="{self.char}"'


class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        hashmap = {}
        for vortexes, edge in zip(equations, values):
            first, second = vortexes
            first_node = hashmap.setdefault(first, Node(first))
            second_node = hashmap.setdefault(second, Node(second))

            first_node.neighbors[second_node] = edge
            second_node.neighbors[first_node] = round(1 / edge, 5)

        def dfs_traversal(start: Node, multiplier=1.0) -> int:
            if start.char == divisor:
                return multiplier
            visited.add(start)
            for node, path in start.neighbors.items():
                if node not in visited:
                    tmp = dfs_traversal(node, multiplier * path)
                    if tmp and tmp != -1.0:
                        return tmp
            return -1.0

        result = []
        for dividend, divisor in queries:
            if dividend not in hashmap or divisor not in hashmap:
                result.append(-1.0)
            else:
                visited = set()
                res = dfs_traversal(hashmap[dividend])
                result.append(res)

        return result


if __name__ == '__main__':
    task = Solution()

    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

    print(task.calcEquation(equations, values, queries))
