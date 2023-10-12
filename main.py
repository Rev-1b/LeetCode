class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        storage = {}
        for index, num in enumerate(nums):
            if num in storage and index - storage[num] <= k:
                return True
            storage[num] = index
        return False


nums = [1, 2, 3, 1]
k = 3

if __name__ == '__main__':
    task = Solution()
    print(task.containsNearbyDuplicate(nums, k))
