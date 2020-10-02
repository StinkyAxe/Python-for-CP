
# ! Find the Rotation Count in Rotated Sorted array

# * The no of times an array must be rotated to make it perfectly sorted

# TODO : Find pivot and rotation will be pivot index + 1

# * Returns pivot
def findRotation(arr,low,high):

    if low == high:
        return low
    mid = (low+high)//2

    if low < mid and arr[mid] > arr[mid+1]:
        return mid
    elif high > mid and arr[mid] < arr[mid-1]:
        return mid-1
    else:
        if arr[0]<arr[mid]:
            return findRotation(arr, mid+1, high)
        else:
            return findRotation(arr, low, mid-1)

if __name__ == '__main__':
    myList = list(map(int, input().split()))
    ans = findRotation(myList,0,len(myList)-1)
    # * Prints the rotation required = pivot + 1
    print("Rotations required:",ans+1)