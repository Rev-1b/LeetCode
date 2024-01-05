from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow, fast = head, head.next

        while fast and fast.next:
            if slow == fast:
                return True

            slow = slow.next
            fast = fast.next.next

        return False


if __name__ == '__main__':
    task = Solution()

    node1 = ListNode(1)
    node2 = ListNode(2, node1)
    node3 = ListNode(3, node2)
    node4 = ListNode(4, node3)
    node5 = ListNode(5, node4)
    node6 = ListNode(6, node5)
    node7 = ListNode(7, node6)
    node8 = ListNode(8, node7)
    node9 = ListNode(9, node8)
    node10 = ListNode(10, node9)

    node4.next = node9

    print(task.hasCycle(node10))
