from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        head = None
        tail = None

        while l1 and l2:
            if l1.val <= l2.val:
                node = ListNode(l1.val)
                l1 = l1.next if l1 else None
            else:
                node = ListNode(l2.val)
                l2 = l2.next if l2 else None

            if not head:
                head = node
                tail = head
            else:
                tail.next = node
                tail = node

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return head


if __name__ == '__main__':
    task = Solution()

    node8 = ListNode(9)
    node7 = ListNode(8, node8)
    node5 = ListNode(7, node7)
    node3 = ListNode(6, node5)
    node1 = ListNode(5, node3)

    node9 = ListNode(4)
    node6 = ListNode(3, node9)
    node4 = ListNode(2, node6)
    node2 = ListNode(1, node4)

    print(task.mergeTwoLists(node1, node2))
