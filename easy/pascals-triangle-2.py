"""
Q - https://leetcode.com/problems/pascals-triangle-ii/

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it
0 <= rowIndex <= 33
Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
"""

from typing import List


class Solution:
    """
    Generate Pascal's Triangle upto rowIndex through a nested for loop per element per row
    Return the last row

    To get space complexity of O(rowIndex):
    Realise that rowIndex is the length of the row in question
    Then we must re-use the same row array when we add elements 
    """

    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        print(row)
        return row


sol = Solution()
sol.getRow(5)
