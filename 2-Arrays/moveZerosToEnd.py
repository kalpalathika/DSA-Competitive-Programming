"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

link - https://leetcode.com/problems/move-zeroes/description/
"""

from ast import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0

        for i in range(len(nums)):
            if(nums[i] != 0):

                nums[j] , nums[i] = nums[i] , nums[j]
                print(i,j,nums[i],nums[j])
                j += 1



        # arrayWithoutZeroCount = []
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         arrayWithoutZeroCount.append(nums[i])
        # j = 0
        # while j < len(arrayWithoutZeroCount):
        #     nums[j] = arrayWithoutZeroCount[j]
        #     j += 1
        # while j < len(nums):
        #     nums[j] = 0
        #     j += 1