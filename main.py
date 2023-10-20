from typing import Optional
from test import print_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'value = {self.val}'


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root

        while curr:
            if curr.left:
                temp = curr.left

                while temp.right:
                    temp = temp.right

                temp.right = curr.right
                curr.left, curr.right = None, curr.left
            curr = curr.right


if __name__ == '__main__':
    task = Solution()

    node1 = TreeNode(1)
    node2 = TreeNode(2, node1)
    node4 = TreeNode(4)
    node3 = TreeNode(3, node2, node4)
    node6 = TreeNode(6)
    node7 = TreeNode(7, node6)
    node5 = TreeNode(5, node3, node7)
    node12 = TreeNode(12)
    node10 = TreeNode(10)
    node11 = TreeNode(11, node10, node12)
    node9 = TreeNode(9, None, node11)
    node8 = TreeNode(8, node5, node9)

    inorder = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    postorder = [1, 2, 4, 3, 6, 7, 5, 10, 12, 11, 9]
    preorder = [8, 5, 3, 2, 1, 4, 7, 6, 9, 11, 10, 12]

    print_tree(node8)
    print('\n\n------------------------------------------------\n\n')
    task.flatten(node8)
    print_tree(node8)
