arr = [1,2,3,4]
n = len(arr)

def search(arr,index,n,key):
    ans = 0    
    if n == 0:
        return -1
    if arr[index] == key:
        return index  
    return search(arr,index + 1,n-1,key)
    # return ans
    

print(search(arr,0,n,10))