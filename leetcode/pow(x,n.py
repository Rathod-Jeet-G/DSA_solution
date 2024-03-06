x = 2.00000
n = -2
nn = n
ans = 1.0
for i in range(n):
    if n>0:
        ans = ans*x
    if(n<0):
        x = x*x
        nn = nn//2
        ans = 1.0/nn

print(ans)