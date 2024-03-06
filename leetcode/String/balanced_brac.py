def balancedBreac(s):
    stack = []
    for i in range(len(s)):
        if s[i] == "(" or s[i] == "{" or s[i] == "[":
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return False
            else:
                char = stack[-1]
                stack.pop()
                if s[i] == ")" and char == "(":
                    continue
                if s[i] == "]" and char == "[":
                    continue
                if s[i] == "}" and char == "{":
                    continue
                else:
                    return False
    if len(stack) == 0:
        return True
    return False


def main():
    s = "(())"
    if balancedBreac(s):
        print("string is balanced")
    else:
        print("string is not balanced")    

main()