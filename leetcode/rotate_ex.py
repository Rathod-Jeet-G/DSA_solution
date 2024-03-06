l = [[1,2,3],[4,5,6],[7,8,9]]

n = len(l)

for i in range(n):
    for j in range(i):
        l[i][j],l[j][i] = l[j][i],l[i][j]
    # l[i].reverse()
for i in range(len(l)):
    l[i].reverse()
print(l)