def subset(arr,index,output,ans):
    #Base Case
    if index>=len(arr):
        ans.append(output[:])
        return

    #Exclude
    subset(arr,index+1,output,ans)

    #Include
    element = arr[index]
    output.append(element)
    # print(output)
    subset(arr,index+1,output,ans)
    output.pop() # element pop for new subset
    # print("after pop:",output)

arr = [1,2,3]
ans = []
output = []
subset(arr,0,output,ans)

print(ans)