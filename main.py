from typing import Optional
from collections import deque
from helper import build_tree, print_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'value = {self.val}'


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev_value = float('-inf')
        curr = root

        while True:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            elif not stack:
                return True
            else:
                node = stack.pop()
                if node.val <= prev_value:
                    return False
                curr = node.right
                prev_value = node.val


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

    # inorder = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # postorder = [1, 2, 4, 3, 6, 7, 5, 10, 12, 11, 9]
    # preorder = [8, 5, 3, 2, 1, 4, 7, 6, 9, 11, 10, 12]

    temp6 = TreeNode(6)
    temp3 = TreeNode(3)
    temp4 = TreeNode(4, temp3, temp6)
    temp1 = TreeNode(1)
    temp5 = TreeNode(5, temp1, temp4)

    print_tree(temp5)


    print(task.isValidBST(temp5))
