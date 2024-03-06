nums = [1,2,3,1]
n = len(nums)
k = 3
val = 0
dict = {}
for i in range(len(nums)):
    if nums[i] in dict:
        if i - dict[nums[i]] <= k:
            print(True)
        else:
            dict[nums[i]] = i
    else:
        dict[nums[i]] = i
# print(False)
print(dict[nums])

# j = k+1
# while(k<=n):
#     if j>n:
#         j=0
#     if nums[k] == nums[j]:
#         print(True)
#     else:
#         print(False)
#     j+=1
