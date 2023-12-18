class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        pos_list, neg_list, zero = [], [], 0
        result = set()

        for elem in nums:
            if elem < 0:
                neg_list.append(elem)
            elif elem > 0:
                pos_list.append(elem)
            else:
                zero += 1

        pos_set, neg_set = set(pos_list), set(neg_list)

        if zero >= 3:
            result.add((0, 0, 0))

        if zero:
            for pos_num in pos_set:
                if -1 * pos_num in neg_set:
                    result.add((-1 * pos_num, 0, pos_num))

        def do_magic(num_list: list[int], num_set: set[int]) -> None:
            for i in range(len(num_list)):
                for j in range(i + 1, len(num_list)):
                    target = -1 * (num_list[i] + num_list[j])
                    if target in num_set:
                        result.add(tuple(sorted([num_list[i], target, num_list[j]])))

        do_magic(pos_list, neg_set)
        do_magic(neg_list, pos_set)

        return result


if __name__ == '__main__':
    task = Solution()
    print(task.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
