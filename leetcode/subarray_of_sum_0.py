def subArray(arr,n):
    maxlen = 0
    hashMap = {}
    sum1 = 0

    for i in range(n):
        sum1+=arr[i]
        if sum1 == 0:
            maxlen = max(maxlen,i+1)
        else:
            if sum1 in hashMap:
                maxlen = max(maxlen,i-hashMap[sum1])
            else:
                hashMap[sum1] = i
    return maxlen

def main():
    arr = list(map(int,input().split(" ")))
    print(subArray(arr,len(arr)))

main()