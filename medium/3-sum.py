"""
Q - https://leetcode.com/problems/3sum/
A - 

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
0 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []

    triplets = []

    # Find distinct triplets summing to 0
    # Approach 3. For each n, compute pair sum, search for three-sum - O(n*logn^2)
    for i in range(len(nums)):
        for j in range(i+1):
            pair_sum = nums[i] + nums[j]
            third = -pair_sum
            for k in nums[j+1:]:
                if third == k:
                    triplets.append([i, j, k])

    return triplets
