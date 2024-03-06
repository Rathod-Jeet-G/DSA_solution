def issorted(arr,size):
    if size == 0 or size == 1:
        return True
    elif arr[0] > arr[1]:
        return False
    else:
        ans = issorted(arr[1:],size - 1)
        return ans

def main():
    arr = [1,2,3,10,5,6,7,8]
    ans = issorted(arr,len(arr))
    if(ans):
        print("Array is Sorted")
    else:
        print("Array is not Sorted")

main()