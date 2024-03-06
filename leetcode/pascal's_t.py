numsrow = 5

ans = []
for i in range(numsrow):
    temp=[]
    for j in range(i+1):
        if j==0 or j==i:
            temp.append(1)
        else:
            temp.append(ans[i-1][j] + ans[i-1][j-1])
    ans.append(temp)
print(ans)