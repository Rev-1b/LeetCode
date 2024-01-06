from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        curr = head
        storage = {}
        i = 1

        while curr:
            storage[i] = curr
            curr = curr.next
            i += 1

        list_len = i - 1
        k = k % list_len
        if not k:
            return head

        storage[list_len - k].next = None
        storage[list_len].next = head
        return storage[list_len - k + 1]



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
