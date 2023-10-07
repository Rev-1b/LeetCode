class Solution:
    def maxArea(self, height: list[int]) -> int:
        ln = len(height) - 1
        i, j = 0, ln
        max_square = min(height[0], height[-1]) * ln

        while i < j:
            ln -= 1
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
            if min(height[i], height[j]) * ln > max_square:
                max_square = min(height[i], height[j]) * ln

        return max_square


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

if __name__ == '__main__':
    task = Solution()
    print(task.maxArea(height))
