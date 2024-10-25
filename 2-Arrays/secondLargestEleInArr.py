"""
Given an array arr, return the second largest element from an array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the first largest.

Examples:

Input: arr = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.
Input: arr = [10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist..
Constraints:
2 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105

link - https://www.geeksforgeeks.org/problems/second-largest3735/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=second-largest
"""

class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        maxFirst = float('-inf')
        maxSecond = float('-inf')
        for i in range(len(arr)):
            if(arr[i] > maxFirst):
                maxFirst = arr[i]
        for j in range(len(arr)):
            if(arr[j] > maxSecond and arr[j] < maxFirst ):
                maxSecond = arr[j]
        if(maxSecond == float('-inf') or maxFirst == float('-inf')):
            return -1
        return maxSecond
    
#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends