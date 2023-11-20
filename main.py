import heapq


class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        heap = []
        heapq.heapify(heap)

        for i in range(min(len(nums1), k)):
            heapq.heappush(heap, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))

        result = []
        while k > 0 and heap:
            _, num1, num2, index = heapq.heappop(heap)
            result.append((num1, num2))

            if index + 1 < len(nums2):
                heapq.heappush(heap, (num1 + nums2[index + 1], num1, nums2[index + 1], index + 1))

            k -= 1

        return result


nums1 = [1, 2]
nums2 = [3]
k = 2

if __name__ == '__main__':
    task = Solution()
    print(task.kSmallestPairs(nums1, nums2, k))
