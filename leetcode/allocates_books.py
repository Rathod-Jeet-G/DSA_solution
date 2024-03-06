def solution(arr,page):
    studentcnt = 1
    pagescnt = 0
    for i in range(len(arr)):
        if pagescnt + arr[i]<=page:
            pagescnt+=arr[i]
        else:
            studentcnt +=1
            pagescnt = arr[i]
    return studentcnt
def allocte(arr,m):
    low = max(arr)
    high = sum(arr)
    while low<=high:
        mid = (low + high)//2
        cnt = solution(arr,mid)
        if cnt<=m:
            high = mid-1
        else:
            low = mid+1
    return low

def main():
    arr = [2, 1, 5, 6, 2, 3]
    m = 2
    print(allocte(arr,m))

main()