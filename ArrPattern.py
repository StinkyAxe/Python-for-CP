
# ! Rearrange array such that :
# ! arr[i] >= arr[j] if i is even 
# ! arr[i] <= arr[j] if i is odd and j < i

# TODO : Sort the array and travel alternate position from left
# TODO:  to right and then from right to left

def makeArr(arr):
    n = len(arr)
    temp = arr.copy()
    temp.sort()

    mid = (0+n-1)//2
    
    i = mid
    for j in range(0,n,2):
        arr[j] = temp[i]
        i-=1
    i = mid+1
    for j in range(1,n,2):
        arr[j] = temp[i]
        i+=1

    return arr


if __name__ == '__main__':
    myList = list(map(int, input().split()))
    ans = makeArr(myList)
    print(ans)