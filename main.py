from typing import Optional


class ListNode:
    def __init__(self, x: int, next: 'ListNode' = None):
        self.val = int(x)
        self.next = next

    def __str__(self):
        return f'Val = {self.val}'


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temporal = ListNode(-1)
        temporal.next = head
        prev = temporal
        curr = head

        while curr:
            while curr.next and curr.next.val == curr.val:
                curr = curr.next
            if prev.next == curr:
                prev = prev.next
                curr = curr.next
            else:
                prev.next = curr.next
                curr = prev.next

        return temporal.next






if __name__ == '__main__':
    n7 = ListNode(5)
    n6 = ListNode(4, n7)
    n5 = ListNode(3, n6)
    n4 = ListNode(3, n5)
    n3 = ListNode(2, n4)
    n2 = ListNode(1, n3)
    n1 = ListNode(1, n2)

    task = Solution()
    head1 = task.deleteDuplicates(n1)
    while head1:
        print(head1.val)
        head1 = head1.next
