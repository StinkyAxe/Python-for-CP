
# ! Left Rotation

# TODO : Juggling Algorithm

def gcd(a, b): 
    if b == 0: 
        return a; 
    else: 
        return gcd(b, a % b) 

def leftRotate(arr, d): 
    n = len(arr)
    d = d % n
    count = gcd(d,n)
    for i in range(count):
        temp = arr[i]
        j = i
        while(True):
            idx = (j+d)%n
            if(idx == i):
                break
            arr[j] = arr[idx]
            j = idx
        arr[j] = temp
    return arr

if __name__ == '__main__':
    myList = list(map(int, input().split()))
    n = int(input())
    ans = leftRotate(myList,n)
    print(ans)