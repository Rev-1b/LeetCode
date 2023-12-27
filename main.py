from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        cache = defaultdict(list)

        for index, num in enumerate(nums):
            if num in cache and index - cache[num][-1] <= k:
                return True
            cache[num].append(index)
        return False


if __name__ == '__main__':
    task = Solution()
    print(task.containsNearbyDuplicate(nums=[1, 2, 3, 5, 1], k=3))
