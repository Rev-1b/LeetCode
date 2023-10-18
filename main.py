from typing import Optional


class ListNode:
    def __init__(self, x: int, next: 'ListNode' = None):
        self.val = int(x)
        self.next = next

    def __str__(self):
        return f'Val = {self.val}'


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l_head, l_tail = None, None
        gbb_head, gbb_tail = None, None
        e_head, e_tail = None, None
        gaa_head, gaa_tail = None, None
        curr = head
        result = None

        while curr:
            if curr.val < x:
                if not l_head:
                    l_head = curr
                    l_tail = l_head
                else:
                    l_tail.next = curr
                    l_tail = curr

            elif curr.val > x:
                if e_head:
                    if not gaa_head:
                        gaa_head = curr
                        gaa_tail = gaa_head
                    else:
                        gaa_tail.next = curr
                        gaa_tail = curr
                else:
                    if not gbb_head:
                        gbb_head = curr
                        gbb_tail = gbb_head
                    else:
                        gbb_tail.next = curr
                        gbb_tail = curr
            else:
                if not e_head:
                    e_head = curr
                    e_tail = e_head
                else:
                    e_tail.next = curr
                    e_tail = curr
            curr = curr.next

        if l_head:
            result = l_head
            if gbb_head:
                l_tail.next = gbb_head
                gbb_tail.next = e_head
            else:
                l_tail.next = e_head
        elif gbb_head:
            result = gbb_head
            gbb_tail.next = e_head

        if gaa_head:
            e_tail.next = gaa_head
            gaa_tail.next = None
        else:
            e_tail.next = None

        return result


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
