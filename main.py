from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        prev = None
        prev_res = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            num = (val1 + val2 + prev_res) % 10
            prev_res = (val1 + val2 + prev_res) // 10
            obj = ListNode(num)

            if not head:
                head = obj
                prev = head
            else:
                prev.next = obj
                prev = obj

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if prev_res:
            prev.next = ListNode(prev_res)
        return head


if __name__ == '__main__':
    num1 = ListNode(1)
    num2 = ListNode(0, num1)
    num3 = ListNode(0, num2)
    # num4 = ListNode(9)
    num5 = ListNode(9)
    num6 = ListNode(9, num5)

    task = Solution()
    head1 = task.addTwoNumbers(num3, num6)
    while head1:
        print(head1.val)
        head1 = head1.next
