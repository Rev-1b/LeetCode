from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head.next

        while fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False


if __name__ == '__main__':
    d = ListNode(1)
    c = ListNode(2, d)
    b = ListNode(3, c)
    a = ListNode(4, b)

    task = Solution()
    print(task.hasCycle(a))
