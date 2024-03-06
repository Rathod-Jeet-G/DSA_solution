x = 121

temp = x
sum = 0
while(x>0):
    r = x%10
    sum = (sum*10)+r
    x = x//10
if temp == sum:
    print("it is palindrom")
else:
    print("it is not palindrom")