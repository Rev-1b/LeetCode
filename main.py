class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        def check_3Sum(collection, alter_coll_set):
            for i in range(len(collection)):
                for j in range(i + 1, len(collection)):
                    target = -1 * (collection[i] + collection[j])
                    if target in alter_coll_set:
                        result.add(tuple(sorted([collection[i], collection[j], target])))

        result = set()
        negative, positive, zero = [], [], 0
        for num in nums:
            if num > 0:
                positive.append(num)
            elif num < 0:
                negative.append(num)
            else:
                zero += 1

        neg_set, pos_set = set(negative), set(positive)
        if zero:
            for num in neg_set:
                if -1 * num in pos_set:
                    result.add((-1 * num, 0, num))

        if zero >= 3:
            result.add((0, 0, 0))

        check_3Sum(negative, pos_set)
        check_3Sum(positive, neg_set)

        return result


nums = [-1, 0, 1, 2, -1, -4]

if __name__ == '__main__':
    task = Solution()
    print(task.threeSum(nums))
