a = [1,2,3,4,5,6,7,8,9,10]
n = len(a)

def binary_search(a,l,r,k):
    if l>r:
        return -1
    mid = (l + r)//2
    # print(mid)
    if a[mid] == k:
        return mid
    if a[mid]<k:
        return binary_search(a,mid+1,r,k)
    else:
        return binary_search(a,l,mid-1,k)

print(binary_search(a,0,n-1,2))
    
