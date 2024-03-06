def one_to_n(n):
    if n == 0:
        return   
    print(n)
    one_to_n(n-1)
    
print(one_to_n(5))