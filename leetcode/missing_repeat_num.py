def find_num(arr,n):
    count = [0]*(n+1)
    for i in range(n):
        count[arr[i]] +=1
    print(count)
    duplicate,missing = -1,-1
    for i in range(1,n+1):
        if count[i] == 2:
            duplicate = i
        elif count[i] == 0:
            missing = i
    
    return [duplicate,missing]


def main():
    arr = [1,2,3,2]
    print(find_num(arr,len(arr)))

main()
