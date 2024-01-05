from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        tail = None
        prev_val = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            temp_sum = val1 + val2 + prev_val
            new_node_val = temp_sum % 10
            prev_val = temp_sum // 10

            new_node = ListNode(new_node_val)
            if not head:
                head = new_node
                tail = head
            else:
                tail.next = new_node
                tail = new_node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if prev_val:
            tail.next = ListNode(prev_val)

        return head


if __name__ == '__main__':
    task = Solution()

    node1 = ListNode(1)
    node2 = ListNode(2, node1)
    node3 = ListNode(3, node2)
    node4 = ListNode(4, node3)
    node5 = ListNode(5, node4)
    node6 = ListNode(6, node5)
    node7 = ListNode(7, node6)
    node8 = ListNode(8, node7)
    node9 = ListNode(9, node8)
    node10 = ListNode(10, node9)

    node4.next = node9

    print(task.addTwoNumbers(node10))
