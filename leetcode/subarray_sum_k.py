from collections import defaultdict

def totalSubarray(arr,k):
    n = len(arr)
    presum = 0
    mapp = defaultdict(int)
    mapp[0] = 1
    cnt = 0
    for i in range(n):
        presum+=arr[i]
        print("presum: ",presum)
        rem = presum-k
        print("mapp: ",mapp)
        cnt+=mapp[rem]
        mapp[presum] += i
        print("mapp: ",mapp)
        
    return cnt

def main():
    arr = [3,-3,1,1,1]
    k = 3
    print(totalSubarray(arr,k))

main()
