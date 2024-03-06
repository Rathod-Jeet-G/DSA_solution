def minimum(arr,n):
    low = 0
    high = n-1
    minimum_no = float('inf')
    while(low <= high):

        mid = (low + high)//2

        if arr[low]<=arr[mid]:
            minimum_no = min(minimum_no,arr[low])
            low = mid+1
        else:
            minimum_no = min(minimum_no,arr[mid])
            high = mid-1
    return minimum_no

def main():
    arr = [4,5,6,7,0,1,2]

    print(minimum(arr,len(arr)))

main()