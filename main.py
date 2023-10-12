class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        hash_map = set(nums)
        biggest = 1
        curr = 1
        temp_elem = hash_map.pop()

        while hash_map:
            if temp_elem - 1 in hash_map:
                hash_map.add(temp_elem)
                temp_elem = temp_elem - 1
            elif temp_elem + 1 in hash_map:
                curr += 1
                biggest = max(biggest, curr)
                if temp_elem in hash_map:
                    hash_map.remove(temp_elem)
                temp_elem = temp_elem + 1
            else:
                temp_elem = hash_map.pop()
                curr = 1
        return biggest



nums = [100, 4, 200, 1, 3, 2]

if __name__ == '__main__':
    task = Solution()
    print(task.longestConsecutive(nums))
