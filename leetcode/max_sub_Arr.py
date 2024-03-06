

nums = [-2,1,-3,4,-1,2,1,-5,4]

sum = nums[0]
temp = nums[0]

for i in range(len(nums)):
    temp = temp + nums[i]
    if temp>sum:
        sum = temp

    if temp<0:
        temp = 0



# sum = nums[0]
# temp = nums[0]
# i = 0
# j = 1
# k = 0
#
# while(j<len(nums)):
#     if(temp<=0):
#         while(k<len(nums) and nums[k]>=0):
#             k = k+1
#         i = k
#         j = i+1
#         temp = nums[k]
#         sum = max(sum,temp)
#
#     else:
#         temp = temp + nums[j]
#         j+=1
#         sum = max(sum,temp)

print(sum)