from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        stack = [(root, root)]

        while stack:
            curr_p, curr_q = stack.pop()
            if not curr_p and not curr_q:
                continue
            if curr_p.val != curr_q.val or \
                    curr_p.left and not curr_q.right or \
                    curr_q.left and not curr_p.right or \
                    curr_p.right and not curr_q.left or \
                    curr_q.right and not curr_p.left:
                return False

            stack.append((curr_p.left, curr_q.right))
            stack.append((curr_p.right, curr_q.left))

        return True


if __name__ == '__main__':
    task = Solution()

    node4 = TreeNode(7)
    node3 = TreeNode(15)
    node2 = TreeNode(20, node3, node4)
    node1 = TreeNode(9)
    root = TreeNode(3, node1, node2)

    print(task.invertTree(root))
