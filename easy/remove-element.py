"""
Q - https://leetcode.com/problems/remove-element/

Given an integer array nums and an integer val, 
remove all occurrences of val in nums in-place. 
The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, 
you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, 
then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. 
You must do this by modifying the input array in-place with O(1) extra memory.
"""
from typing import List


class Solution:
    """
    Human Method
    nums = [1,2,1]
    val = 2
    res = [1,1,_], k=2

    nums = [1,1,2,3,2]
    val = 2
    res = [1,1,3,_,_], k=2

    Explanation
    Initalise slow and fast pointer
    Move fast and slow along until value matched
    Move fast along until non-value matched
    Update slow^th elem with fast
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            if nums[left] != val:
                left += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1

        return left


sol = Solution()
sol.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
