
# ! Given a sorted and rotated array, find if there is a pair
# ! with a given sum

# TODO: Find pivot and apply 2 pointers algorithm

# * Finding the pivot of the array
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

# * To check if any pair exist which equals the sum
def findPair(arr,low,high,sumx):
    # * If this is not given, maximum recursion depth will exceed
    if low == high:
        return 0
    # * Pair exist checking condition
    if arr[low] + arr[high] == sumx:
        return True
    elif arr[low] + arr[high] < sumx:
        # * For cyclic flow
        if low == len(arr)-1:
            low = low-len(arr)
        return findPair(arr,low+1,high,sumx)
    elif arr[low] + arr[high] > sumx:
        # * For cyclic flow
        if high == 0:
            high = len(arr)-high
        return findPair(arr,low,high-1,sumx)
    else:
        pass

if __name__ == '__main__':
    myList = list(map(int, input().split()))
    sumx = int(input())
    low = 0
    high = len(myList)-1
    ans = findPivot(myList,low,high)
    if findPair(myList,ans+1,ans,sumx):
        print("Pair exists!")
    else:
        print("Pair doesn't exist!")
    