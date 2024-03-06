a = [1,2,3,1,1,1,1]
n = len(a)
k = 3
temp = []

i = 0
j = n-1

while(i<=j):
    sum=a[i]+a[j]
    while sum<=k and i<j:
        temp.append(a[i])
        temp.append(a[j])
        j-=1
    i+=1
    # j-=1
    

print(temp)