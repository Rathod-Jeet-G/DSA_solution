nums = [1,3,4,2,2]
#
# for i in range(len(nums)):
#     if nums[i] == nums[i+1]:
#         ans = nums[i]
#         break
# i = 0
# while(i<len(nums)):
#     if nums[i] == nums[i+1]:
#         ans = nums[i]
#         break
#     i+=1
# print(ans)

slow = nums[0]
fast = nums[0]

while True:
    slow = nums[slow]
    fast = nums[nums[fast]]
    print(fast)
    #
    # if nums[slow] == nums[fast]:
    #     break
    # fast = nums[0]

# while slow!=fast:
#     slow = nums[slow]
#     fast = nums[fast]
# print(fast)