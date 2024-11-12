
class Solution:
    def binarySearch(self,sortedArr,key):
        i = 0
        j = len(sortedArr) - 1

        while i <= j:
            middleIndex = (i+j)//2
            if key == sortedArr[middleIndex]:
                return True
            if key > sortedArr[middleIndex]:
                i = middleIndex + 1
            else:
                j = middleIndex - 1

        return False

bs = Solution()
print(bs.binarySearch([1,2,3,4,8,9,10,24],5))
print(bs.binarySearch([1,2,3,4,8,9,10,24],9))
print(bs.binarySearch([1,2,3,4,8,9,10,24],24))


