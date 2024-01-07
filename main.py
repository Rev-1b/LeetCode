from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_node = ListNode(x=-1)
        temp_node.next = head
        curr = head

        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return temp_node.next


if __name__ == '__main__':
    task = Solution()

    node8 = ListNode(9)
    node7 = ListNode(8, node8)
    node5 = ListNode(8, node7)
    node3 = ListNode(5, node5)
    node1 = ListNode(5, node3)

    node9 = ListNode(2, node1)
    node6 = ListNode(2, node9)
    node4 = ListNode(2, node6)
    node2 = ListNode(2, node4)

    print(task.deleteDuplicates(node2))
