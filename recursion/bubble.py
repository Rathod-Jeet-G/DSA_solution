def sortArray(arr,n):
    if n==0 or n==1:
        return
    
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]

    return sortArray(arr,n-1)

arr = [5,3,5,1,4,2,0]

sortArray(arr,len(arr))

print(arr)