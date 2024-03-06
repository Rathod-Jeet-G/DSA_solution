def largeOddNum(s):
    for i in range(len(s)-1,-1,-1):
        if int(s[i]) %2 == 1:
            return s[:i+1]
    return ""
        
    

def main():
    s = "35427"
    print(largeOddNum(s))

main()