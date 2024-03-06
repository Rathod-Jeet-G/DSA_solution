def solve(digit,output,index,ans,mapp):
    if index>=len(digit):
        ans.append(output[:])
        return

    number = int(digit[index])
    
    val =  mapp[number]

    for i in range(len(val)):
        output += val[i]
        solve(digit,output,index+1,ans,mapp)
        output=output[:-1]
    # for char in val:
    #     solve(digit, output + char, index + 1, ans, mapp)

digit = "23"
def latter(digit):
    ans  = []
    if len(digit) == 0:
        return ans
    output = ""
    index = 0
    mapp = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    solve(digit,output,index,ans,mapp)
    return ans

print(latter(digit))
    