"""
Given an Integer n and a list arr. Sort the array using bubble sort algorithm.

Examples :

Input: n = 5, arr[] = {4, 1, 3, 9, 7}
Output: 1 3 4 7 9
Input: n = 10, arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
Output: 1 2 3 4 5 6 7 8 9 10

Your Task : 
You don't have to read input or print anything. Your task is to complete the function bubblesort() which takes the array and it's size as input and sorts the array using bubble sort algorithm.
Constraints:
1 <= n <= 103
1 <= arr[i] <= 103

link - https://www.geeksforgeeks.org/problems/bubble-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=bubble-sort
"""
class Solution:
    def bubbleSort(self,arr, n):
        # code here
        for i in range(len(arr)):
            for j in range(len(arr) - 1 - i):
                if(arr[j] > arr[j+1]):
                    arr[j], arr[j +1] = arr[j +1], arr[j]
            
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr, n)
        for i in arr:
            print(i,end=' ')
        print()

# } Driver Code Ends