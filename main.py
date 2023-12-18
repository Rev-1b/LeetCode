class Solution:
    def maxArea(self, height: list[int]) -> int:
        i, j = 0, len(height) - 1
        result = min(height[i], height[j]) * (j - i)

        while i < j:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            result = max(min(height[i], height[j]) * (j - i), result)

        return result


if __name__ == '__main__':
    task = Solution()
    print(task.maxArea(height=[1, 2, 4, 3]))
