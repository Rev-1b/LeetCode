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
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        def do_magic(inorder):
            nonlocal preorder

            if not preorder:
                return None

            value = preorder[0]
            if value not in inorder:
                return None
            preorder = preorder[1:]
            value_pos = inorder.index(value)
            node = TreeNode(value)

            if len(inorder) > 1:
                node.left = do_magic(inorder[:value_pos])
                node.right = do_magic(inorder[value_pos + 1:])
            return node

        return do_magic(inorder)


if __name__ == '__main__':
    task = Solution()

    # node4 = TreeNode(7)
    # node3 = TreeNode(15)
    # node2 = TreeNode(20, node3, node4)
    # node1 = TreeNode(9)
    # root = TreeNode(3, node1, node2)

    preorder1 = [9, 5, 3, 2, 1, 4, 7, 6, 12, 15, 13, 20]
    inorder1 = [1, 2, 3, 4, 5, 6, 7, 9, 12, 13, 15, 20]

    preorder2 = [1, 2]
    inorder2 = [2, 1]

    root = task.buildTree(preorder1, inorder1)
    print_tree(root)
