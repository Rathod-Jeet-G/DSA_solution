arr = [1,2,3]

n = len(arr)
def nextPermutation(arr,n):
    ind =-1
    for i in range(n-2,-1,-1):
        if arr[i] < arr[i+1]:
            ind = i
            break
    if ind  == -1:
        arr.reverse()
    for i in range(n-1,ind,-1):
        if arr[i]>arr[ind]:
            arr[i],arr[ind] = arr[ind],arr[i]
            break
    arr[ind+1:] = reversed(arr[ind+1:])
    return arr

print(nextPermutation(arr,len(arr)))