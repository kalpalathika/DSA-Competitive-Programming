"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

link - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

"""

from typing import List


class Solution:
    def getEndingIndex(self,arr,k):
        i = 0
        j = len(arr) - 1
        index = -1
        while i <= j:
            middle = (i+j)//2
            if arr[middle] <= k:
                if arr[middle] == k:
                    index = middle
                i = middle + 1
            else: 
                j = middle - 1
        return index

    def getStartingIndex(self,arr,k):
        i = 0
        j = len(arr) - 1
        index = -1
        while i <= j:
            middle = (i+j)//2
            if arr[middle] >= k:
                if arr[middle] == k:
                    index = middle
                j = middle - 1
            else: 
                i = middle + 1
        return index

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.getStartingIndex(nums,target)
        if start > - 1:
            end = self.getEndingIndex(nums,target) 
            return [start,end]
        return [-1,-1]
    
bs = Solution()
print(bs.searchRange([5,7,7,8,8,10],8))