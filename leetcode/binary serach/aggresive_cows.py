def posiblecows(stalls,dist,cow):
    cntcow=1
    last = stalls[0]
    n = len(stalls)
    for i in range(1,n):
        if stalls[i]-last >= dist:
            cntcow+=1
            last = stalls[i]
        if cntcow>=cow:
            return True
    return False

def aggresiveCows(stalls,cow):
    n = len(stalls)
    limit = stalls[n-1]-stalls[0]
    low = 1
    high = limit
    stalls.sort()
    while low<=high:
        mid = (low + high)//2

        if posiblecows(stalls,mid,cow):
            low = mid+1
        else:
            high = mid-1

    return high 

def main():
    stalls = [0,3,4,7,11,9]
    cow = 4
    print(aggresiveCows(stalls,cow))

main()