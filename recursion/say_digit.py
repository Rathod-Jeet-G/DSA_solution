def saydigit(n,arr):
    if n == 0:
        return
    digit = n%10
    n = n//10

    saydigit(n,arr)

    print(arr[digit],end=" ")

arr = ['Zero','One','Two','Three','Four','Five','six','seven','eight','nine']
n = int(input())
print(saydigit(n,arr))

