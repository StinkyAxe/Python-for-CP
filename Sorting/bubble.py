def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(arr[i]< arr[j]):
                arr[i],arr[j] = arr[j], arr[i]

if __name__ == "__main__":
    n = int(input("Enter no of elements: "));
    array = list(map(int, input().split()))
    bubble(array)
    for i in array:
        print(i, end=" ")
    print()
