l1 = [1,2,1,4,2,1,3,2,6]
n = len(l1)
hashh = [0]*n
for i in l1:
    if i in hashh:
        hashh[l1[i]] +=1
    else:
        hashh[l1[i]] = 1
def count(num,hashh):
    return hashh[num]

print("counter of each elemnt in hash:",hashh)
print(count(1,hashh)) 