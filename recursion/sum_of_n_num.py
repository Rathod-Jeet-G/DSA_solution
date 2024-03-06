def addition(i,sum):
    if i<1:
        print(sum)
        return
    addition(i-1,sum+i)
addition(3,0)

# using function equation we can solve the n number elements sums

def add2(n):
    if n==0:
        return 0
    return n+add2(n-1)

print("using functional recursion",str(add2(3)))
