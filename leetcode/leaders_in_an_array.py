def leadersInArray(arr,n):
    ans = []
    max_no = 0
    for i in range(n-1,-1,-1):
        if arr[i] > max_no:
            ans.append(arr[i])
        max_no = max(max_no,arr[i])

    return ans

def main():
    arr = [10,22,12,3,0,6]
    print(leadersInArray(arr,len(arr)))

main()