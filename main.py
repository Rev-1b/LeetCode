from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        if not nums:
            return
        node_index = len(nums) // 2
        node = TreeNode(nums[node_index])
        node.left = self.sortedArrayToBST(nums[:node_index])
        node.right = self.sortedArrayToBST(nums[node_index + 1:])
        return node


if __name__ == '__main__':
    task = Solution()

    nums1 = [-10, -3, 0, 5, 9]

    print(task.sortedArrayToBST(nums1))
