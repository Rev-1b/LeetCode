class Solution:
    def jump(self, nums: list[int]) -> int:
        ans = 0
        end = 0
        farthest = 0

        # Implicit BFS
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                ans += 1
                break
            if i == end:  # Visited all the items on the current level
                ans += 1  # Increment the level
                end = farthest  # Make the queue size for the next level

        return ans


if __name__ == '__main__':
    task = Solution()

    nums = [2, 3, 1, 1, 4]

    print(task.jump(nums))
