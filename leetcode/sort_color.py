nums = [2,0,2,1,1,0]
i = 0
j = len(nums)-1

while(i<j):
    while(nums[i]==0):
        i+=1
    while(nums[j]!=0):
        j-=1
    nums[i],nums[j] = nums[j],nums[i]

while(i<len(nums)):
    if(nums[i]==0):
        i+=1
while (i < j):
    while (nums[i] == 1):
        i += 1
    while (nums[j] != 1):
        j -= 1
    nums[i], nums[j] = nums[j], nums[i]

print(nums)