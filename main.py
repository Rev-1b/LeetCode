from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and not q or q and not p:
            return False
        stack = [(p, q)]

        while stack:
            curr_p, curr_q = stack.pop()
            if not curr_p and not curr_q:
                continue
            if curr_p.val != curr_q.val or \
               curr_p.left and not curr_q.left or \
               curr_q.left and not curr_p.left or \
               curr_p.right and not curr_q.right or \
               curr_q.right and not curr_p.right:
                return False

            stack.append((curr_p.left, curr_q.left))
            stack.append((curr_p.right, curr_q.right))

        return True


if __name__ == '__main__':
    task = Solution()

    node4 = TreeNode(7)
    node3 = TreeNode(15)
    node2 = TreeNode(20, node3, node4)
    node1 = TreeNode(9)
    root = TreeNode(3, node1, node2)

    print(task.maxDepth(root))
