def GeneratePermutation(arr,index,ans):
    
    if index>=len(arr):
        ans.append(arr[:])
        return
    
    for i in range(index,len(arr)):
        arr[i],arr[index] = arr[index],arr[i]
        GeneratePermutation(arr,index+1,ans)
        arr[i],arr[index] = arr[index],arr[i]
    return ans

ans = []
arr=[1,2,3]
print(GeneratePermutation(arr,0,ans))
