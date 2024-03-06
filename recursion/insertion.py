def insertion_Sort(arr,i,n):
    if i == n:
        return
    
    j = i
    while(j>0 and arr[j-1]>arr[j]):
        arr[j-1],arr[j] = arr[j],arr[j-1]
        j-=1
    insertion_Sort(arr,i+1,n)

arr = [5,3,5,1,4,2,0]

insertion_Sort(arr,0,len(arr))

print(arr)  


    