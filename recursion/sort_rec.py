a = [5,4,62,2,7,1]

n = len(a)
swap = True
def asc(i,j,n):
    while(swap):
        swap = False
        if j>=n or i>=n:
            return
        if a[i]>a[j]:
            a[i],a[j] = a[j],a[i]
            swap = True
            asc(i + 1, j + 1,n-1)
        asc(i+1,j+1,n-1)
asc(0,1,n)
print(a)