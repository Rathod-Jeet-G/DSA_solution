def serachMatrix(matrix,k):
    row = len(matrix)
    col = len(matrix[0])
    low = 0
    high = row*col-1
    while low<=high:
        mid = (low + high)//2
        r = mid//col
        c = mid%col
        if matrix[r][c] == k:
            return True
        if matrix[r][c]>k:
            high = mid-1
        else:
            low = mid+1
    return False

def main():
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    k = 3
    print(serachMatrix(matrix,k))

main()