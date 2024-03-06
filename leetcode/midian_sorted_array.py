def midianSortedArray(nums1,nums2):
    left = 0
    right = 0
    n1 = len(nums1)
    n2 = len(nums2)
    nums3 = []
    while left < n1 and right < n2:
        if nums1[left] < nums2[right]:
            nums3.append(nums1[left])
            left+=1
        else:
            nums3.append(nums2[right])
            right+=1
    while left<n1:
        nums3.append(nums1[left])
        left+=1
    while right<n2:
        nums3.append(nums2[right])
        right+=1
    
    n = n1+n2
    if n%2 == 1:
        return float(nums3[n//2])

    median = (nums3[n//2] + nums3[(n//2)-1])/2
    return median
    # print(nums3)
    # low = nums3[0]
    # high = nums3[len(nums3)-1]
    # mid = (low + high)/2
    # print(mid)

def main():
    arr1 = [1,3]
    arr2 = [2]
    print(midianSortedArray(arr1,arr2))

main()       