from typing import Optional


class ListNode:
    def __init__(self, x: int, next: 'ListNode' = None):
        self.val = int(x)
        self.next = next

    def __str__(self):
        return f'Val = {self.val}'




class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        curr = head
        tail = None
        while left > 1:
            tail = curr
            curr = curr.next
            left -= 1
            right -= 1

        first_to_last = curr
        prev = None
        while right > 0:
            next_node = curr.next
            if prev:
                curr.next = prev
            prev = curr
            curr = next_node
            right -= 1

        if tail:
            tail.next = prev
        else:
            head = prev
        first_to_last.next = curr
        return head


if __name__ == '__main__':
    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)

    task = Solution()
    head1 = task.reverseBetween(n1, 1, 4)
    while head1:
        print(head1.val)
        head1 = head1.next
