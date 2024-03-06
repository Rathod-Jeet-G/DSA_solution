# the below recursion function is not work for whitespace string
def ispalindrom(i,j,s):
    if i>j:
        return True
    if s[i] != s[j]:
        return False
    else:
        return ispalindrom(i+1,j-1,s)
    
s = 'abbebba'
# sl = list(s)
isp = ispalindrom(0,len(s)-1,s)
if(isp):
    print("it is palindrom")
else:
    print("it is not palindrom")