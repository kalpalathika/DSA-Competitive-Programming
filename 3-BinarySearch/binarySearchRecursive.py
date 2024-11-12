
class Solution:
    def __binarySearch(self,sortedArr,key,i, j):

        if i > j:
            return False
        middleIndex = (i+j) // 2
        if key == sortedArr[middleIndex]:
            return True
        if key > sortedArr[middleIndex]:
            return self.__binarySearch(sortedArr,key,middleIndex + 1, j)
        elif key < sortedArr[middleIndex]:
            return self.__binarySearch(sortedArr,key,i , middleIndex - 1)
        
    def binarySearch(self,sortedArr,key):
        i = 0
        j = len(sortedArr) - 1

        return self.__binarySearch(sortedArr, key, i,j)

bs = Solution()
print(bs.binarySearch([1,2,3,4,8,9,10,24],5))
print(bs.binarySearch([1,2,3,4,8,9,10,24],9))
print(bs.binarySearch([1,2,3,4,8,9,10,24],24))


