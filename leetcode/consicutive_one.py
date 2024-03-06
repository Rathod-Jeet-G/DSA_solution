nums = [1,1,0,1,1,1]
n = len(nums)

cnt = 0
for i in range(n):
    if nums[i]==1:
        cnt+=1
    else:
        cnt = 0
print(cnt)
