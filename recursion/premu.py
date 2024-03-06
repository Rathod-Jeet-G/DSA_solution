a = [1,2,3]
n = len(a)
ans = []
def recursion(ind,nums):
    if ind == n:
        ans.append(nums[:])
        return
    # i = ind
    for i in range(ind,n):
        nums[i],nums[ind] = nums[ind],nums[i]
        recursion(ind+1,nums)
        nums[i], nums[ind] = nums[ind], nums[i]

recursion(0,a)
print(ans)