"""
Given a sorted array arr[] (with unique elements) and an integer k, find the index (0-based) of the largest element in arr[] that is less than or equal to k. This element is called the "floor" of k. If such an element does not exist, return -1.

Examples

Input: arr[] = [1, 2, 8, 10, 11, 12, 19], k = 0
Output: -1
Explanation: No element less than 0 is found. So output is -1.
Input: arr[] = [1, 2, 8, 10, 11, 12, 19], k = 5
Output: 1
Explanation: Largest Number less than 5 is 2 , whose index is 1.
Input: arr[] = [1, 2, 8], k = 1
Output: 0
Explanation: Largest Number less than or equal to  1 is 1 , whose index is 0.
Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 106
0 ≤ k ≤ arr[n-1]

link - https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1?track=DSASP-Searching&amp%253BbatchId=154&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=floor-in-a-sorted-array
"""


class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,arr,k):
        #Your code here
        i = 0
        j = len(arr) - 1
        
        while i <= j:
            middleIndex = (i+j)//2
            # equals, less than , index == last element case
            if (arr[middleIndex]) == k or (middleIndex < len(arr) - 1 and arr[middleIndex] < k and arr[middleIndex+1] > k) or (middleIndex == len(arr) - 1 and arr[middleIndex] < k):
                    return middleIndex
            
            if k < arr[middleIndex]:
                j = middleIndex - 1
            elif k > arr[middleIndex]:
                i = middleIndex + 1
        
        return -1
bs = Solution()
print(bs.findFloor([1, 2, 8, 10, 11, 12, 19],5))