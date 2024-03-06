def unique_sum(arr,n):
    freq = {}
    for i in range(n):
        if arr[i] in freq:
            freq[arr[i]] +=1
        else:
            freq[arr[i]] = 1
    # return freq

    arr2 = []
    for key,val in freq.items():
        if val == 1:
            arr2.append(key)
    ans = 0
    for i in range(len(arr2)):
        ans+=arr2[i]
    return ans
    


arr = [1,2,3,1]
print(unique_sum(arr,len(arr)))