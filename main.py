class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_x = 0
        curr = x

        while curr > 0:
            digit = curr % 10
            reversed_x = reversed_x * 10 + digit
            curr //= 10

        return x == reversed_x


x = 121
if __name__ == '__main__':

    task = Solution()
    print(task.isPalindrome(x))
