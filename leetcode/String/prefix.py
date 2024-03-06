def longesPrefix(s):
    ans = ""
    for i in range(len(s[0])):
        firstchar = s[0][i]
        match = True
        for j in range(1,len(s)):
            if len(s[j]) < i or firstchar != s[j][i]:
                match = False
                break
        if(match == False):
            break
        else:
            ans += firstchar
    return ans


def main():
    s = ["flower","flow","flight"]
    print(longesPrefix(s))

main()