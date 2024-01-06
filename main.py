from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


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
    task = Solution()

    # node8 = ListNode(9)
    # node7 = ListNode(8, node8)
    # node5 = ListNode(7, node7)
    # node3 = ListNode(6, node5)
    # node1 = ListNode(5, node3)
    #
    # node9 = ListNode(4)
    # node6 = ListNode(3, node9)
    # node4 = ListNode(2, node6)
    # node2 = ListNode(1, node4)

    print(task.copyRandomList())
