# def fun(i,n):
#     if i<1:
#         return
#     fun(i-1,n)
#     print(i)
# fun(6,10)


#back track n to 1
def fun1(i,n):
    if i>n:
        return
    fun1(i+1,n)
    print(i)
fun1(1,10)