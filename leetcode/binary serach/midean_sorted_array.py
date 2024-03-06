def median(a,b):
    n1 = len(a)
    n2 = len(b)
    if n1>n2:
        return median(b,a)
    n = n1 + n2
    left = (n1 + n2 + 1)//2
    low,high = 0,n1
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
            if n % 2 == 1:
                return max(float(l1),float(l2))
            else:
                return (float(max(l1,l2)) + (min(r1,r2)))/2
        elif l1>r1:
            high = mid1-1
        else:
            low = mid1+1
   
    return 0

def main():
    a = [1,3,4,7,10,12]
    b = [2,3,6,15]
    print(median(a,b))

main() 