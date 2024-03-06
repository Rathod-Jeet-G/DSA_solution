import math
def calculate_hourse(arr,hourse):
    calth = 0
    n = len(arr)
    for i in range(n):
        calth += math.ceil(arr[i]/hourse)
    return calth

def minEatingSpeed(piles,h):
    low, high, ans = 1, max(piles), max(piles)
    while low<=high:
        mid = (low + high)//2
        calth = calculate_hourse(piles,mid)
        if calth<=h:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans

def main():
    arr = list(map(int,input().split(" ")))
    h = int(input())
    print(minEatingSpeed(arr,h))

main()
