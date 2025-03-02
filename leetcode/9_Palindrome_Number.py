class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''Given an integer x, return true if x is a palindrome, and false otherwise.
        >>> Solution().isPalindrome(121)
        True

        >>> Solution().isPalindrome(-121)
        False

        >>> Solution().isPalindrome(10)
        False

        >>> Solution().isPalindrome(1000021)
        False
        '''
        x = str(x)
        length = len(x)
        for i in range(length // 2):
            if x[i] != x[length - i - 1]:
                return False
        return True




if __name__ == '__main__':
    import doctest

    doctest.testmod()
