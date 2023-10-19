from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(depth, max_depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return max_depth


if __name__ == '__main__':
    task = Solution()

    node4 = TreeNode(7)
    node3 = TreeNode(15)
    node2 = TreeNode(20, node3, node4)
    node1 = TreeNode(9)
    root = TreeNode(3, node1, node2)

    print(task.maxDepth(root))
