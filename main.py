import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        return heap[0]


if __name__ == '__main__':
    task = Solution()

    nums = [3, 2, 1, 5, 6, 4]

    print(task.findKthLargest(nums, 2))
