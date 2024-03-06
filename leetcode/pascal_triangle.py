def pascal(RowIndex):
    ans = []
   
    for i in range(RowIndex):
        temp = []
        for j in range(i+1):
            if j == 0 or j==i:
                temp.append(1)
            else:
                temp.append(ans[i-1][j]+ ans[i-1][j-1])
        ans.append(temp)
    return ans

def main():
    rowIndex = 5
    print(pascal(rowIndex))

main()
