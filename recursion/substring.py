def solve(string,index,output,ans):
    if index>=len(string):
        if len(output)>0:
            ans.append(output)
        return
    
    solve(string,index+1,output,ans)

    output += string[index]
    
    solve(string,index+1,output,ans)
    output = output[:-1]
    return ans 


    
     

string = "xyz"
ans = []
index = 0
output = ""
solve(string,index,output,ans)
for i in ans:
    print(i)
