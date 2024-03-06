str = "race a car"
# l1 = list(str)
n=len(str)
def pel(i):
    if i>=n/2:
        return True
    if str[i] != str[n-i-1]:
        return False
    return pel(i+1)


if pel(0) == False:
    print("given string is not palindrom")
else:
    print("given string is palindrom")

#print(l1)

