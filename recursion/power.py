def power(a,b):
    print("a:",a,"b:",b)
    if b == 0:
        return 1
    if b == 1:
        return a
    ans = power(a,b//2)
    print("ans",ans)
    if b%2 == 0:
        return ans*ans
    else:
        return a*ans*ans
    
print(power(2,22))