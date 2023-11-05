from random import choice


class RandomizedSet:

    def __init__(self):
        self.data_map = {}
        self.data_list = []

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False
        self.data_list.append(val)
        self.data_map[val] = len(self.data_list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data_map:
            return False

        last_elem = self.data_list[-1]
        val_indx = self.data_map[val]
        self.data_map[last_elem] = val_indx
        self.data_list[val_indx] = last_elem

        self.data_list[-1] = val
        self.data_list.pop()
        self.data_map.pop(val)
        return True

    def getRandom(self) -> int:
        return choice(self.data_list)

if __name__ == '__main__':
    # task = Solution()
    #
    # nums = [3, 2, 1, 5, 6, 4]
    #
    #
    # print(task.hIndex(nums))
    pass
