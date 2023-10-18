from typing import Optional


class ListNode:
    def __init__(self, x: int, next: 'ListNode' = None):
        self.val = int(x)
        self.next = next

    def __str__(self):
        return f'Val = {self.val}'


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before, after = ListNode(0), ListNode(0)
        before_curr, after_curr = before, after

        while head:
            if head.val < x:
                before_curr.next, before_curr = head, head
            else:
                after_curr.next, after_curr = head, head
            head = head.next

        after_curr.next = None
        before_curr.next = after.next

        return before.next


if __name__ == '__main__':
    n7 = ListNode(2)
    n6 = ListNode(1, n7)
    n5 = ListNode(8, n6)
    n4 = ListNode(4, n5)
    n3 = ListNode(5, n4)
    n2 = ListNode(6, n3)
    n1 = ListNode(3, n2)

    task = Solution()
    head1 = task.partition(n1, 2)
    while head1:
        print(head1.val, end=' ')
        head1 = head1.next
