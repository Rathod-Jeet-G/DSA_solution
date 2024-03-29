def generatePascalTriangel(rowIndex):
    pascal = []
    for i in range(rowIndex+1):
        temp = []
        for j in range(i+1):
            if j == 0 or j==i:
                temp.append(1)
            else:
                temp.append(pascal[i-1][j] + pascal[i-1][j-1])
        pascal.append(temp)
    return pascal[rowIndex]
        
def main():
    print(generatePascalTriangel(3))

main()
