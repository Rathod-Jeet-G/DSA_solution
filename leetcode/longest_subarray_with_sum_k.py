def longestsubarray(arr,n,k):
    maxLen,sum1 = 0,0
    preSum = {} #it store the previous sum with index

    for i in range(n):
        sum1 +=arr[i]
        if sum1 == k:
            maxLen = max(maxLen,i+1)
        rem = sum1 - k
        if rem in preSum:
            length = i-preSum[rem]
            maxLen = max(maxLen,length)
        if sum1 not in preSum:
            preSum[sum1] = i
    
    return maxLen

arr = [1, 2, 1, 0, 1]
n = len(arr)
k = 4

print(longestsubarray(arr,n,k))
