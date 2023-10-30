class Solution:
    def permute(self, nums1: list[int]) -> list[list[int]]:
        if len(nums1) == 1:
            return [nums1]

        nums1 = set(nums1)
        result = []

        def do_magic(nums: set[int], prev: list[int]) -> None:
            if len(nums) == 1:
                result.append([*prev, *nums])
                return

            for num in nums:
                nums_copy = nums.copy()
                nums_copy.remove(num)
                do_magic(nums_copy, [*prev, num])

        do_magic(nums1, [])
        return result


if __name__ == '__main__':
    task = Solution()

    nums2 = [1, 2, 3, 4]

    print(task.permute(nums2))
