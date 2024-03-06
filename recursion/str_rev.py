def rev_str(i,j,s):
    if i>=j:
        return ''.join(s)
    s[i],s[j] = s[j],s[i]
    return rev_str(i+1,j-1,s)

s = 'jeet'
str_list = list(s)
n = len(str_list)
rev_string= rev_str(0,n-1,str_list)
print(rev_string)