"""
Q - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.

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
    EXAMPLE 
    [1,2] -> [1,2], k=2
    [1,1,2] -> [1,2,_] k=2
    [1,1,2,2,3] -> [1,2,3,_,_], k=3

    PSEUDOCODE
    1. slow pointer sits at ith elem
    2. fast pointer moves until non-duplicate reached
    3. ith elem replaced with non-duplicate
    4. slow pointer increment
    5. repeat until end of array reached
    6. Return slow pointer position as k

    O(n) time, O(n) space
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        slow, fast = 1, 0

        while fast < len(nums)-1:
            if nums[fast] == nums[fast+1]:
                fast += 1
            else:
                fast += 1
                nums[slow] = nums[fast]
                slow += 1

        print(nums[:slow])
        return slow


s = Solution()
s.removeDuplicates([1, 1, 2, 2, 3])
