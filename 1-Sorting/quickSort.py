"""
Quick Sort is a Divide and Conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot.
Given an array arr[], its starting position is low (the index of the array) and its ending position is high(the index of the array).

Note: The low and high are inclusive.

Implement the partition() and quickSort() functions to sort the array.

Example 1:

Input: 
N = 5 
arr[] = { 4, 1, 3, 9, 7}
Output:
1 3 4 7 9
Example 2:

Input: 
N = 9
arr[] = { 2, 1, 6, 10, 4, 1, 3, 9, 7}
Output:
1 1 2 3 4 6 7 9 10
Your Task: 
You don't need to read input or print anything. Your task is to complete the functions partition()  and quickSort() which takes the array arr[], low and high as input parameters and partitions the array. Consider the last element as the pivot such that all the elements less than(or equal to) the pivot lie before it and the elements greater than it lie after the pivot.

Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(logN)

Constraints:
1 <= N <= 103
1 <= arr[i] <= 104

link - https://www.geeksforgeeks.org/problems/quick-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=quick-sort
"""


class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low < high:  
            pivot_index = self.partition(arr,low,high)
            self.quickSort(arr,low,pivot_index-1)
            self.quickSort(arr,pivot_index + 1, high)
        return arr
        
    
    def partition(self,arr,low,high):
        pivot = low
        i = low + 1
        swap = low
        
        while(i <= high):
            if(arr[i] < arr[pivot]):
                swap += 1
                arr[swap] , arr[i] = arr[i] , arr[swap]
            i += 1
        arr[pivot], arr[swap] = arr[swap] , arr[pivot]
        return swap
        # code here

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

        print("~")
# } Driver Code Ends