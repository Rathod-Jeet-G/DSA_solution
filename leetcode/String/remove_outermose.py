def reomveOuter(s):
    stack = []
    sub = ""
    for i in range(len(s)):
        char = s[i]
        if char == "(":
            if len(stack)>0:
                sub+=char
            stack.append(char)
        else:
            stack.pop()
            if len(stack)>0:
                sub+=char
    return sub

def main():
    s = "(()())(())(()(()))"
    print(reomveOuter(s))

main()