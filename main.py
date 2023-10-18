from typing import Optional
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.data: OrderedDict[int, int] = OrderedDict()
        self.capacity: int = capacity

    def get(self, key: int) -> int:
        return -1 if key not in self.data else self.data.setdefault(key, self.data.pop(key))

    def put(self, key: int, value: int) -> None:
        try:
            self.data.move_to_end(key)
            self.data[key] = value
        except KeyError:
            self.data[key] = value
            if len(self.data) > self.capacity:
                self.data.popitem(last=False)


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
