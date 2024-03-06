def isIsomorphic(s1,s2):
    maps1,maps2 = {},{}
    for i in range(len(s1)):
        c1,c2 = s1[i],s2[i]
        print(c1,c2)
        if (c1 in maps1 and maps1[c1] != c2) or (c2 in maps2 and maps2[c2]!=c1):
            return False
        maps1[c1] = c2
        maps2[c2] = c1
        print("maps1",maps1,"and",maps2)
    return True

    
    # print(hashMap)

def main():
    s1 = "badc"
    s2 = "baba"
    print(isIsomorphic(s1,s2))

main()