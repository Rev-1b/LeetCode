from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before, after = ListNode(0), ListNode(0)
        before_curr, after_curr = before, after

        while head:
            if head.val < x:
                before_curr.next = head
                before_curr = head

            else:
                after_curr.next = head
                after_curr = head

            head = head.next

        after_curr.next = None
        before_curr.next = after.next

        return before.next


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
