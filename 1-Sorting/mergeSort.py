"""
Given an array arr[], its starting position l and its ending position r. Sort the array using the merge sort algorithm.

Examples:

Input: arr[] = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]
Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Constraints:
1 <= arr.size() <= 105
1 <= arr[i] <= 105

"""


#User function Template for python3

class Solution:
    def merge(self,arr, l, m, r): 
        i = l
        j = m + 1
        combined = []
        while i <=m and j <= r:
            if(arr[i] < arr[j]):
                combined.append(arr[i])
                i += 1
            else:
                combined.append(arr[j])
                j += 1
        
        while(i <= m):
            combined.append(arr[i])
        while(j <= r):
            combined.append(arr[j])
        return combined
        
    def mergeSort(self,arr, l, r):
        #code here
        if l >= r:
            return
        m = (l + r)//2
        self.mergeSort(arr,l,m)
        self.mergeSort(arr,m + 1, r)
        return self.merge(arr,l,m,r)

