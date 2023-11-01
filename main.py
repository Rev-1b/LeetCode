from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'val={self.val}'


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        left_node = head
        right_node = self.get_mid(head)
        tmp = right_node.next
        right_node.next = None
        right_node = tmp

        left_node = self.sortList(left_node)
        right_node = self.sortList(right_node)

        res = self.merge(left_node, right_node)
        return res

    def get_mid(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, list1, list2):
        new_head = tail = ListNode()
        while True:
            if not list1:
                tail.next = list2
                break

            if not list2:
                tail.next = list1
                break

            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        return new_head.next


if __name__ == '__main__':
    task = Solution()

    node0 = ListNode(val=0)
    node4 = ListNode(val=4, next=node0)
    node3 = ListNode(val=3, next=node4)
    node5 = ListNode(val=5, next=node3)
    node_1 = ListNode(val=-1, next=node5)

# [-1,5,3,4,0]

    print(task.sortList(node_1))
