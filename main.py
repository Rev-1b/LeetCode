from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_head = head
        new_head = Node(old_head.val)
        new_tail = new_head
        old_to_new = {old_head: new_head}
        old_head = old_head.next

        while old_head:
            obj = Node(old_head.val)
            old_to_new[old_head] = obj
            new_tail.next = obj
            new_tail = obj
            old_head = old_head.next

        while head:
            old_to_new.get(head).random = old_to_new.get(head.random)
            head = head.next

        return new_head


if __name__ == '__main__':

    task = Solution()
    head1 = task.copyRandomList()
    while head1:
        print(head1.val)
        head1 = head1.next
