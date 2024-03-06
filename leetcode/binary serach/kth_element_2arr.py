def kthel(a,b,n1,n2,k):
    if n1>n2:
        return kthel(b,a,n2,n1,k)
    left = k
    low = max(0,k-n2)
    high = min(k,n1)
    n = n1+n2
    while low<=high:
        mid1 = (low + high)//2
        mid2 = left - mid1
        l1,l2 = float('-inf'),float('-inf')
        r1,r2 = float('inf'),float('inf')
        if mid1<n1:
            r1 = a[mid1]
        if mid2<n2:
            r2 = b[mid2]
        if mid1-1>=0:
            l1 = a[mid1-1]
        if mid2-1>=0:
            l2 = b[mid2-1]
        if l1<=r2 and l2<=r1:
            return max(l1,l2)
        elif l1>r2:
            high = mid1-1
        else:
            low = mid1+1
    return 0

def main():
    a = [2,3,6,7,9]
    b = [1,4,8,10]
    k = 5
    print(kthel(a,b,len(a),len(b),k))

main()


