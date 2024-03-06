def search(arr,n,k):
    low = 0
    high = n-1

    while low<=high:
        mid = (low + high)//2

        if arr[mid] == k:
            return mid
        if arr[low] <= arr[mid]:
            if arr[low]<=k and arr[mid]>=k:
                high = mid-1
            else:
                low = mid+1
        else:
            if arr[mid]<=k and arr[high] >= k:
                low = mid+1
            else:
                high = mid-1
    return -1
    
def main():
    arr = [4,5,6,7,0,1,2]
    t = 0
    print(search(arr,len(arr),t))

main()