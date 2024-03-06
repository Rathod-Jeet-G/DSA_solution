def partition(arr,low,high):
    pivot = arr[low]
    i=low
    j=high
    while i<j:
        while arr[i]<=pivot and i<=high-1:
            i+=1
        while arr[j]>pivot and j>=low+1:
            j-=1
        if i<=j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[low],arr[j]= arr[j],arr[low]
    return j

        
def QuickSort(arr,low,high):
    if low<high:
        p = partition(arr,low,high)
        QuickSort(arr,low,p-1)
        QuickSort(arr,p+1,high)

arr = [5,3,5,1,4,2,0]

QuickSort(arr,0,len(arr)-1)

print(arr)  