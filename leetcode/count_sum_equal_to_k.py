from collections import defaultdict


def countSubArray(arr,n,k):
    hashMap = defaultdict(int)
    cnt = 0
    preSum = 0
    hashMap[0] = 1
    for i in range(len(arr)):
        preSum += arr[i]
        rem = preSum - k
        cnt += hashMap[rem]
        hashMap[preSum] += 1
    
    return cnt

def main():
    arr = [1,2,3]
    k = 3
    print("Total subArray are:",countSubArray(arr,len(arr),k))

main()

