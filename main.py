from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        curr, i = head, 1
        storage = {}

        while curr:
            storage[i] = curr
            curr = curr.next
            i += 1

        length = i - 1
        k = k % length

        if not k:
            return head

        storage.get(length - k).next = None
        storage.get(length).next = head
        return storage[length - k + 1]


if __name__ == '__main__':
    task = Solution()

    node8 = ListNode(9)
    node7 = ListNode(8, node8)
    node5 = ListNode(8, node7)
    node3 = ListNode(5, node5)
    node1 = ListNode(5, node3)

    node9 = ListNode(2, node1)
    node6 = ListNode(2, node9)
    node4 = ListNode(2, node6)
    node2 = ListNode(2, node4)

    print(task.deleteDuplicates(node2))
