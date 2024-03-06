st="abcabsbaba"
size = 26
hashh = [0]*size
ascii = ord('a')
# print(ascii)
hashdi = {}

for i in st:
    if i in hashdi:
        hashdi[i]+=1
    else:
        hashdi[i]=1



for i in range(len(st)):
    hashh[ord(st[i])-ord('a')] += 1
    


print("using list",hashh)
print('using dictonary',hashdi)