"""
The task is to complete the insert() function which is used to implement Insertion Sort.


Examples:

Input: n = 5, arr[] = { 4, 1, 3, 9, 7}
Output: 1 3 4 7 9
Input: n = 10, arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
Output: 1 2 3 4 5 6 7 8 9 10

Your Task: 
You don't have to read input or print anything. Your task is to complete the function insert() and insertionSort() where insert() takes the array, it's size and an index i and insertionSort() uses insert function to sort the array in ascending order using insertion sort algorithm. 

Expected Time Complexity: O(n*n).
Expected Auxiliary Space: O(1).


Constraints:
1 <= n <= 1000
1 <= arr[i] <= 1000

link - https://www.geeksforgeeks.org/problems/insertion-sort/0?category%5B%5D=Algorithms&page=1&query=category%5B%5DAlgorithmspage1&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=insertion-sort
"""
class Solution:
    def insert(self, alist, index, n):
        #code here
        if index == n :
            return
        else:
            for i in range(index,0,-1):
                if(alist[i] <  alist[i-1]):
                    alist[i], alist[i-1] = alist[i-1], alist[i]
            self.insert(alist,index + 1, n)
                
                
                
       
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
           return self.insert(alist,1,n)
           

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        Solution().insertionSort(arr, n)

        for i in range(n):
            print(arr[i], end=" ")

        print()

# } Driver Code Ends