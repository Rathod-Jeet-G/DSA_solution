def sortArray(arr,n):
    if n == 0 or n==1:
        return
     
    for i in range(n-1):
        mini = i
        if arr[i+1] < arr[mini]:
            mini = i+1
        arr[i],arr[mini] = arr[mini],arr[i]
    
    return sortArray(arr,n-1)

arr = [5,3,5,1,4,2,0]

sortArray(arr,len(arr))

print(arr)  