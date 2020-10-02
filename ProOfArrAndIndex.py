
# ! Find maximum value of Sum( i*arr[i] )
# ! with only rotations on given array allowed

# TODO : Apply S = S' - C + (n*arr[i-1])
# where S = new sum, S' = previous sum, C = sum of array elems
# arr[i-1] = array elem which goes from left to right
# n = array size

def maxSum(arr):
    n = len(arr)
    C = sum(arr)
    maxs = 0
    start = 0
    temp = 0
    for i in arr:
        start += i * arr.index(i)
    temp=start
    for i in range(1, n):
        temp = temp - C + (n*arr[i-1])
        if temp>maxs:
            maxs = temp
    
    return maxs


if __name__ == '__main__':
    myList = list(map(int, input().split()))
    ans = maxSum(myList)
    print(ans)