
# ! Search an element in a sorted and rotated array
# ! In O(logn) time complexity.

# TODO: Find pivot and apply binary search in 2 separate array!

# * Finding the pivot where the next element is smaller than
# * the current element or the current element is smaller than the
# * previous element. The index of the last highest element in
# * between the list is called pivot.
# * 3 4 5 6 1 2 => 3 // index of 6
# * 5 6 1 2 3 4 => 1 // index of 6
def findPivot(arr, low,high):
    if high < low:
        return -1
    if high == low:
        return low
    
    mid = (low+high)//2

    if mid < high and arr[mid] > arr[mid+1]:
        return mid
    elif low < mid and arr[mid] < arr[mid-1]:
        return mid-1
    else:
        if arr[low] < arr[mid]:
            return findPivot(arr, mid+1, high)
        else:
            return findPivot(arr, low, mid-1)

# * Applying Binary Search
def binarySearch(arr,low,high,key):
    if low <= high:
        mid = (low+high)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return binarySearch(arr,mid+1,high,key)
        elif arr[mid] > key:
            return binarySearch(arr, low, mid-1, key)
        else:
            pass

if __name__ == '__main__':
    myList = list(map(int, input().split()))
    key = int(input())
    low = 0
    high = len(myList)-1
    ans = findPivot(myList,low,high)
    if myList[ans] == key:
        r = ans
    else:
        if myList[0] <= key:
            r = binarySearch(myList,low,ans-1,key)
        else:
            r = binarySearch(myList,ans+1,high,key)

    print("The index of the key is:",r)
