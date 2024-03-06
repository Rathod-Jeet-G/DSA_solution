def pascalII(rowIndex):
    ans = [1]
    prev = 1
    for i in range(1,rowIndex+1):
        
        next_value = prev * ((rowIndex-i)+1)//i
        print(next_value)
        ans.append(next_value)
        prev = next_value
    return ans

def main():
    numberofrow = 3
    print(pascalII(numberofrow))

main()