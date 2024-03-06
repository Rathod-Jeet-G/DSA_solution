def median(arr,n,m):
    med = []
    for i in range(n):
        for j in range(m):
            med.append(arr[i][j])
    med.sort()  
    print(med)
    return med[(n*m)//2]

def main():
    arr = [[ 1, 5, 7, 9, 11 ],
      [ 2, 3, 4, 8, 9 ],
      [ 4, 11, 14, 19, 20 ],
      [ 6, 10, 22, 99, 100 ],
      [ 7, 15, 17, 24, 28 ]]
    print(median(arr,len(arr),len(arr[0])))

main()