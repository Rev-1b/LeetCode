from typing import Optional


class Node:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next
        self.random = None


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_head = head
        new_head = Node(head.val)
        new_tail = new_head
        old_to_new = {old_head: new_head}
        old_head = old_head.next

        while old_head:
            new_node = Node(old_head.val)
            old_to_new[old_head] = new_node
            new_tail.next = new_node
            new_tail = new_node
            old_head = old_head.next

        while head:
            old_to_new.get(head).random = old_to_new.get(head.random)
            head = head.next

        return new_head



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
