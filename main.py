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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val

        def do_magic(node: TreeNode) -> int:
            nonlocal max_sum
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val

            left_sum = do_magic(node.left)
            right_sum = do_magic(node.right)

            max_sum = max(max_sum, left_sum + right_sum + node.val, left_sum, right_sum)

            return max(left_sum, right_sum) + node.val

        do_magic(root)
        return max_sum


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

    temp2 = TreeNode(-1)
    temp1 = TreeNode(-2, temp2)

    inorder = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    postorder = [1, 2, 4, 3, 6, 7, 5, 10, 12, 11, 9]
    preorder = [8, 5, 3, 2, 1, 4, 7, 6, 9, 11, 10, 12]

    print(task.maxPathSum(temp1))
