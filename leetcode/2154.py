def multi_o(arr,orignal,n):
    i = 0
    while(i<n):
        if arr[i] == orignal:
            orignal = 2*orignal
            i=0
        i+=1
    return orignal

arr = [5,3,6,1,12]
orignal = 3
print(multi_o(arr,orignal,len(arr)))

