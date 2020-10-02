
# ! Left Rotation

# TODO : Reversal Algorithm

def reverseArr(arr):
    start = 0
    end = len(arr)-1
    for i in range(len(arr)//2):
        arr[start], arr[end] = arr[end],arr[start]
        start+=1
        end-=1
    return arr

def leftRotate(arr, d): 
    temp1 = reverseArr(arr[:d])
    temp2 = reverseArr(arr[d:])
    print(temp1,temp2)
    temp1.extend(temp2)
    ans = reverseArr(temp1)
    return ans

if __name__ == '__main__':
    myList = list(map(int, input().split()))
    n = int(input())
    ans = leftRotate(myList,n)
    print(ans)