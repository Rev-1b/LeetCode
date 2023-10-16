from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        tail = None

        while l1 or l2:
            if not l1:
                obj = ListNode(l2.val)
                l2 = l2.next if l2 else None

            elif not l2:
                obj = ListNode(l1.val)
                l1 = l1.next if l1 else None

            elif l1.val < l2.val:
                obj = ListNode(l1.val)
                l1 = l1.next if l1 else None
            else:
                obj = ListNode(l2.val)
                l2 = l2.next if l2 else None

            if head:
                tail.next = obj
                tail = obj
            else:
                head = obj
                tail = obj

        return head


if __name__ == '__main__':
    num1 = ListNode(12)
    num2 = ListNode(4, num1)
    num3 = ListNode(1, num2)
    num4 = ListNode(5)
    num5 = ListNode(3, num4)
    num6 = ListNode(1, num5)

    task = Solution()
    head1 = task.mergeTwoLists(num3, num6)
    while head1:
        print(head1.val)
        head1 = head1.next
