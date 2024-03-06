nums1 = [1,2,3,0,0,0]
m=3
nums2 = [2,5,6]
n=3
ans = []
left = 0
right = 0
index = 0
while left<m and right<n:
    if nums1[left]<=nums2[right]:
        ans.append(nums1[left])
        left+=1
        index+=1
    else:
        ans.append(nums2[right])
        right+=1
        index+=1
while(left<m):
    ans.append(nums1[left])
    left+=1
    index+=1
while(right<n):
    ans.append(nums2[right])
    right+=1
    index+=1
# for i in range(m+n):
#     if i<m:
#         nums1[i] = ans[i]
#     else:
#         nums1[i] = ans[i]


print(ans)
