class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        back = n + m - 1

        n -= 1
        m -= 1

        while n >= 0:
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[back] = nums1[m]
                m -= 1
            else:
                nums1[back] = nums2[n]
                n -= 1
            back -= 1

        return nums1


if __name__ == '__main__':
    task = Solution()
    print(task.merge(nums1=[0, 0, 0, 0, 0], m=0, nums2=[1, 2, 3, 4, 5], n=3))
