def selectionSort(array):
    curr = array[0]
    for i in range(len(array)):
        mini = min(array[i:])
        array[array.index(mini)],array[i]= array[i],mini
    return array

if __name__ == "__main__":
    n = int(input("Enter no of elements: "));
    array = list(map(int, input().split()))
    sortedArray = selectionSort(array)

    for i in sortedArray:
        print(i, end=" ")
    print()