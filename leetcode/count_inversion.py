a = [3,2,1]
n = len(a)
count = 0

for i in range(n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            count+=1

print(count)