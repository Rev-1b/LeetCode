class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def do_magic(comb: list[int], rest: int, nums: list[int]) -> None:
            for num in nums:
                if rest - num <= 0:
                    if rest - num == 0:
                        result.append([*comb, num])
                    return
                index = nums.index(num)
                do_magic([*comb, num], rest - num, nums[index:])

        do_magic([], target, candidates)
        return result


if __name__ == '__main__':
    task = Solution()

    candidates1 = [2, 3, 6, 7]
    target1 = 7

    print(task.combinationSum(candidates1, target1))
