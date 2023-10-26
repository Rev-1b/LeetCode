from collections import deque
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self):
        return f'val = {self.val}'


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        hashmap = {node.val: Node(node.val, [])}
        deq = deque([node])

        while deq:
            curr = deq.popleft()
            curr_clone = hashmap[curr.val]

            for neighbor in curr.neighbors:
                if neighbor.val not in hashmap:
                    hashmap[neighbor.val] = Node(neighbor.val, [])
                    deq.append(neighbor)
                curr_clone.neighbors.append(hashmap[neighbor.val])

        return hashmap[1]


if __name__ == '__main__':
    task = Solution()

    node4 = Node(4)
    node3 = Node(3)
    node2 = Node(2)
    node1 = Node(1, [node2, node4])
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    task.cloneGraph(node1)
