"""
Q - https://leetcode.com/problems/matrix-cells-in-distance-order/

You are given four integers row, cols, rCenter, and cCenter. 
There is a rows x cols matrix and you are on the cell with the coordinates (rCenter, cCenter).

Return the coordinates of all cells in the matrix, 
sorted by their distance from (rCenter, cCenter) 
from the smallest distance to the largest distance. 
You may return the answer in any order that satisfies this condition.

The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|.
"""

from typing import List


class Solution:
    """
    #1
    Generate all co-ordinates
    Evaluate distance from each
    Sort dictionary
    Extract co-ordinates after sorting

    #2
    Get distance from centre to edge of matrix in all directions
    From rCenter, cCenter, iteratively generate and append co-ordinates in all directions
    Do this until max co-ordinate reached
    """

    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        def dist(point):
            pi, pj = point
            return abs(pi - r0) + abs(pj - c0)

        points = [(i, j) for i in range(R) for j in range(C)]
        return sorted(points, key=dist)


sol = Solution()
sol.allCellsDistOrder(2, 2, 0, 1)
