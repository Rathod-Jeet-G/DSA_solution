def maximum_product_subarray(arr,n):
    prefix = 1
    sufix = 1
    maxpro = float('-inf')

    for i in range(n):
        if prefix == 0:
            prefix = 1
        if sufix == 0:
            sufix =1
        
        prefix *=arr[i]
        sufix *=arr[n-i-1]

        maxpro = max(maxpro,max(prefix,sufix))
    return maxpro
    
def main():
    arr = list(map(int,input().split(" ")))
    print(maximum_product_subarray(arr,len(arr)))

main()