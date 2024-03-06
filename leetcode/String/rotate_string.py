def rotate(s,t):
    n = len(s)
    x = 0
    newchar = ""
    for i in range(len(s)):
        newchar = s[i:] + s[:i]
        if newchar == t:
            return True
       
        print(newchar)
    return False
   

def main():
    s = " bcde"
    print(s[:1])
    goal = "abced"
    print(rotate(s,goal))

main()