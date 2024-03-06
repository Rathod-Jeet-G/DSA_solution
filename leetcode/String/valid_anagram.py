def isAnagram(s,t):
    mapS,mapT = {},{}

    if len(s)!=len(t):
        return False
    for i in range(len(s)):
        mapS[s[i]]= 1+mapS.get(s[i],0)
        mapT[t[i]]= 1+mapT.get(t[i],0)
    
    for char in mapS:
        if mapS[char]!=mapT.get(char,0):
            return False
    return True
    


s = "rat"
t = "car"
print(isAnagram(s,t))     
    
    
