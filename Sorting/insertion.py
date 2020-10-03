def insertionSort(array):
    maxidx = len(array)-1

    for i in range(len(array)):
        j = i
        while(j>0 and array[j-1] > array[j]):
            array[j-1],array[j] = array[j],array[j-1]
            j-=1

    return array

if __name__ == "__main__":
    n = int(input("Enter no of elements: "));
    array = list(map(int, input().split()))
    sortedArray = insertionSort(array)

    for i in sortedArray:
        print(i, end=" ")
    print()