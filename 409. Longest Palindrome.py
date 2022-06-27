# https://leetcode.com/problems/longest-palindrome/
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters_count_dict = {}
        for letter in s:
            if letter in letters_count_dict:
                letters_count_dict[letter] += 1
            else:
                letters_count_dict[letter] = 1
        length_of_palindrome = 0
        for letter, count in letters_count_dict.items():
            if count % 2 == 0:
                length_of_palindrome += count
            else:
                length_of_palindrome += count - 1
        if length_of_palindrome % 2 == 0 and len(s) != length_of_palindrome:
            length_of_palindrome += 1
        return length_of_palindrome


def test():
    assert Solution().longestPalindrome("abccccdd") == 7


if __name__ == '__main__':
    test()
