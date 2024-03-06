li =  [1,2,1,3,1,4,5,6,1,3,1]
hash_map = { }
for i in li:
    if i in hash_map:
        hash_map[i]+=1
    else:
        hash_map[i] = 1

def count_num(num,hash_map):
    if num in hash_map:
        return hash_map[num]
    else:
        # n = 0
        str = "the given number is not present in list"
        return str

print(count_num(1,hash_map))
print(count_num(7,hash_map))
print(hash_map)