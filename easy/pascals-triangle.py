from typing import List

"""
Q - https://leetcode.com/problems/pascals-triangle/

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it

Words:
-Recursive solution by identifying which number is 'above' another and summing them
1. Define base cases
2. Identify parent numbers
3. Sum parent numbers

Efficiency:
runtime O(n^2) given n is numRows, and also length of longest row
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        p = []

        for i in range(numRows):
            row = []

            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(p[i-1][j-1] + p[i-1][j])

            p.append(row)

        print(p)


solution = Solution()
solution.generate(5)
