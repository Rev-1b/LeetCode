from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


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
