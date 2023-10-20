from typing import Optional
from test import print_tree


class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __str__(self):
        return f'value = {self.val}'


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root or not root.left and not root.right:
            return root

        storage = [root]
        while storage:
            temp_storage = []
            prev = None
            for node in storage:
                if prev:
                    prev.next = node
                if node.left:
                    temp_storage.append(node.left)
                if node.right:
                    temp_storage.append(node.right)
                prev = node
            storage = temp_storage
        return root


if __name__ == '__main__':
    task = Solution()

    node8 = Node(5)
    node7 = Node(23)
    node6 = Node(1, node7, node8)
    node5 = Node(6)
    node4 = Node(7)
    node3 = Node(15, node4, node5)
    node2 = Node(20, None, node6)
    node1 = Node(9, node3)
    root = Node(3, node1, node2)

    inorder1 = [1, 2, 3, 4, 5, 6, 7, 9, 12, 13, 15, 20]
    postorder1 = [1, 2, 4, 3, 6, 7, 5, 13, 20, 15, 12, 9]

    preorder2 = [1, 2]
    inorder2 = [2, 1]

    root = task.connect(root)
    print_tree(root)
