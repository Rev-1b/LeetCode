from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root] if root else None

        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root


if __name__ == '__main__':
    task = Solution()

    node4 = TreeNode(7)
    node3 = TreeNode(15)
    node2 = TreeNode(20, node3, node4)
    node1 = TreeNode(9)
    root = TreeNode(3, node1, node2)

    print(task.invertTree(root))
