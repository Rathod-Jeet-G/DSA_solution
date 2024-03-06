def search_in_roted_array(arr,n,x):
    low = 0
    high = n-1

    while low<=high:
        mid = (low + high)//2
        if arr[mid] == x:
            return mid
        if arr[low]<=arr[mid]:
            if arr[low]<=x and x<=arr[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if arr[mid]<=x and x<=arr[high]:
                low = low+1   
            else:
                high = mid-1
                
    return -1

def main():
    arr = list(map(int,input().split(" ")))
    x = int(input())
    print(search_in_roted_array(arr,len(arr),x))
main()