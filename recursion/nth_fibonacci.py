def fibonacii(n):
    n1 = 0
    n2 = 1
    n3 = 0
    for i in range(2,n):
        n3 = n1+n2
        n1 = n2
        n2 = n3
    return n3 
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return 1
    # fibo = fibonacii(n-1) + fibonacii(n-2)
    # return fibo
n = 8
print(fibonacii(n))