
def sum_of_arr(arr,n,ind):
    if n==0:
        return 0
    return arr[ind]+sum_of_arr(arr,n-1,ind+1)    

arr = [5,4,3,2,1]
print(sum_of_arr(arr,len(arr),0)) 