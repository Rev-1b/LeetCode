class Solution:
    def jump(self, nums: list[int]) -> int:
        end, res, curr = 0, 0, 0

        for i in range(len(nums) - 1):
            curr = max(curr, i + nums[i])
            if curr >= len(nums) - 1:
                res += 1
                return res

            if i == end:
                res += 1
                end = curr

        return res


if __name__ == '__main__':
    task = Solution()
    print(task.jump(nums=[2, 3, 1, 1, 4]))
