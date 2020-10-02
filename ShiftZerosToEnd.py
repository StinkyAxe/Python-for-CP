
# ! Move all the zeros to the end of the array in O(n)

def shiftedArray(arr):
    n = len(arr)
    result = list()
    counter = 0

    # * Count the number of elements != 0 and
    # * result[counter] = arr[i] and increment counter
    for i in range(n):
        if(arr[i] != 0):
            result.append(arr[i])
            counter+=1
    
    # * Pad the end with zeros to make same length
    diff = n - len(result)
    result.extend([0] * diff)

    return result

if __name__ =="__main__":
    myList = list(map(int, input().split()))
    ans = shiftedArray(myList)
    for i in ans:
        print(i, end = " ")