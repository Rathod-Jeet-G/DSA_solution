a = [1,2,3,4,5]
n = len(a)
def issorted(a):
    for i in range(n-1):
        if a[i]<=a[i+1]:
            continue
        else: return False
    return True
print(issorted(a))