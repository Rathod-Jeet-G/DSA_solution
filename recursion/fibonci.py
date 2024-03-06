n = 5
a = [0]*n
a[0] = 0
a[1] = 1
i = 2

for i in range(2,n):
    a[i] = a[i-1] + a[i-2]

print("fibonacci number list for", n ,"is:",a)



# def fibo(n):
#     if n<=1:
#         return n
#     return fibo(n-1) + fibo(n-2)
# print(fibo(n))