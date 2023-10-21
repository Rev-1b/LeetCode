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
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[m:] = []
        nums2[n:] = []
        if not nums1:
            nums1.extend(nums2)
            return
        for num in nums2:
            if num <= nums1[0]:
                nums1.insert(0, num)
                continue
            if num >= nums1[-1]:
                nums1.append(num)
                continue

            start, end = 0, len(nums1) - 1
            while start <= end:
                mid = (start + end) // 2
                if nums1[mid - 1] <= num <= nums1[mid]:
                    nums1.insert(mid, num)
                    break
                elif nums1[mid - 1] > num and nums1[mid] > num:
                    end = mid - 1
                else:
                    start = mid + 1

if __name__ == '__main__':
    task = Solution()

    # node1 = TreeNode(1)
    # node2 = TreeNode(2, node1)
    # node4 = TreeNode(4)
    # node3 = TreeNode(3, node2, node4)
    # node6 = TreeNode(6)
    # node7 = TreeNode(7, node6)
    # node5 = TreeNode(5, node3, node7)
    # node12 = TreeNode(12)
    # node10 = TreeNode(10)
    # node11 = TreeNode(11, node10, node12)
    # node9 = TreeNode(9, None, node11)
    # node8 = TreeNode(8, node5, node9)
    #
    # inorder = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # postorder = [1, 2, 4, 3, 6, 7, 5, 10, 12, 11, 9]
    # preorder = [8, 5, 3, 2, 1, 4, 7, 6, 9, 11, 10, 12]

    # print_tree(node8)
    # print('\n\n------------------------------------------------\n\n')
    print(task.hasPathSum(node8, 3))
    # print_tree(node8)
