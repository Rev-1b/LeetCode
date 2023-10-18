from typing import Optional


class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next: Optional[ListNode] = None
        self.prev: Optional[ListNode] = None

    def __str__(self):
        return f'val = {self.val}'


class LinkedList:
    def __init__(self):
        self.head: Optional[ListNode] = None
        self.tail: Optional[ListNode] = None
        self.length = 0

    def place_to_top(self, node: Optional[ListNode]):
        if not node:
            return

        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1

    def remove_node(self, node: Optional[ListNode]):
        if not node:
            return

        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        if self.head == node:
            self.head = node.next

        if self.tail == node:
            self.tail = node.prev

        node.next = None
        node.prev = None
        self.length -= 1


class LRUCache:
    capacity: int
    cache_map: dict[int, ListNode]
    history: LinkedList

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_map = {}
        self.history = LinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache_map:
            return -1

        value_node: ListNode = self.cache_map[key]

        if self.history.head != value_node:
            self.history.remove_node(value_node)
            self.history.place_to_top(value_node)

        return value_node.val

    def put(self, key: int, value: int) -> None:
        value_node: ListNode = ListNode(key, value)

        if key in self.cache_map:
            self.remove_item(self.cache_map[key])

        if len(self.cache_map) >= self.capacity:
            self.evict_least_recent_item()

        self.history.place_to_top(value_node)
        self.cache_map[key] = value_node

    def evict_least_recent_item(self) -> None:
        lru_item: ListNode = self.history.tail

        if lru_item is None:
            return

        self.remove_item(lru_item)

    def remove_item(self, item: ListNode) -> None:
        self.history.remove_node(item)
        del self.cache_map[item.key]
        del item


if __name__ == '__main__':
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    p1 = cache.get(1)
    cache.put(3, 3)
    p2 = cache.get(2)
    cache.put(4, 4)
    p3 = cache.get(1)
    p4 = cache.get(3)
    p5 = cache.get(4)

    print(p1, p2, p3, p4, p5)
    # 1 -1 -1 3 4
