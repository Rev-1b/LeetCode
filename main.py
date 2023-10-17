from typing import Optional


class ListNode:
    def __init__(self, x: int, next: 'ListNode' = None):
        self.val = int(x)
        self.next = next

    def __str__(self):
        return f'Val = {self.val}'


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        storage = {}
        i = 1

        while curr:
            storage[i] = curr
            curr = curr.next
            i += 1

        list_len = i - 1
        k = k % list_len
        if not k:
            return head

        storage[list_len - k].next = None
        storage[list_len].next = head
        return storage[list_len - k + 1]


if __name__ == '__main__':
    n7 = ListNode(7)
    n6 = ListNode(6, n7)
    n5 = ListNode(5, n6)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)

    task = Solution()
    head1 = task.rotateRight(n1, 12)
    while head1:
        print(head1.val)
        head1 = head1.next
