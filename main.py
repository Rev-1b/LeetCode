class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not len(nums):
            return 0

        cache = set(nums)
        result = 1
        temp = 1
        curr = cache.pop()

        while cache:
            if curr - 1 in cache:
                cache.add(curr)
                curr -= 1

            elif curr + 1 in cache:
                temp += 1
                result = max(result, temp)
                if curr in cache:
                    cache.remove(curr)
                curr += 1

            else:
                temp = 1
                curr = cache.pop()

        return result


if __name__ == '__main__':
    task = Solution()
    print(task.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))

    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(sorted(nums))
