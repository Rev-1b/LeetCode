from typing import Optional


class ListNode:
    def __init__(self, x: int, next: 'ListNode' = None):
        self.val = int(x)
        self.next = next

    def __str__(self):
        return f'Val = {self.val}'


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        storage = {}
        i = 1
        curr = head
        while curr:
            storage[i] = curr
            curr = curr.next
            i += 1
        index = i - n
        if index == 1:
            return storage.get(2)
        storage[index - 1].next = storage.get(index + 1)
        return head


if __name__ == '__main__':
    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1)

    task = Solution()
    head1 = task.removeNthFromEnd(n1, 1)
    while head1:
        print(head1.val)
        head1 = head1.next
