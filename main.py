class Solution:
    def maxArea(self, height: list[int]) -> int:
        i, j = 0, len(height) - 1
        prev_max, post_max = height[i], height[j]
        max_square = min(prev_max, post_max) * j

        while i < j:
            if prev_max <= post_max:
                i += 1
                while height[i] <= prev_max and i < j:
                    i += 1
                prev_max = height[i]
            else:
                j -= 1
                while height[j] <= post_max and i < j:
                    j -= 1
                post_max = height[j]

            temp_square = min(prev_max, post_max) * (j - i)
            if temp_square > max_square:
                max_square = temp_square

        return max_square


height = [2, 3, 4, 5, 18, 17, 6]

if __name__ == '__main__':
    task = Solution()
    print(task.maxArea(height))
