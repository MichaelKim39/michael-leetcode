"""
Q - https://leetcode.com/problems/plus-one/

You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1

        while digits[i] == 9 and i >= 0:
            digits[i] = 0
            i -= 1

        if i < 0:
            return [1] + digits
        else:
            digits[i] += 1
            return digits


sol = Solution()
print(sol.plusOne([0]))
