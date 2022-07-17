# https://leetcode.com/problems/plus-one/
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            
            if digits[i] > 9:
                carry = digits[i] // 10
                digits[i] %= 10
            else:
                carry = 0
                break
        if carry == 1:
            digits.insert(0, 1)
        return digits


sol = Solution()
print(sol.plusOne([1,2,3]))