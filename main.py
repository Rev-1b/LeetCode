class Solution:
    def trap(self, height: list[int]) -> int:
        i, j = 0, len(height) - 1
        water = 0
        max_left, max_right = 0, 0
        while i < j:
            if height[i] < height[j]:
                if height[i] >= max_left:
                    max_left = height[i]
                else:
                    water += (max_left - height[i])
                i += 1
            else:
                if height[j] >= max_right:
                    max_right = height[j]
                else:
                    water += (max_right - height[j])
                j -= 1

        return water


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

if __name__ == '__main__':
    task = Solution()
    print(task.trap(height))
