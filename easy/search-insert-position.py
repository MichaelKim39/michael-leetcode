"""
Q - https://leetcode.com/problems/search-insert-position/

Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4

[0,1,2,4,5] <- 3
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binSearch(left, right):
            left, right = 0, len(nums)-1

            while left < right:
                mid = (left + right) // 2
                if target > nums[mid]:
                    left += 1
                else:
                    right = mid

            return right


sol = Solution()
print(sol.searchInsert([1, 3, 5, 6], 5))
