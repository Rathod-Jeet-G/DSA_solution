def RowInd(mat,col):
    maxVal = -1
    maxInd = -1
    for i in range(len(mat)):
        if mat[i][col]>maxVal:
            maxVal = mat[i][col]
            maxInd = i
    return maxInd
def findPeekInMat(mat):
    m = len(mat[0])
    low = 0
    high = m-1
    while low<=high:
        mid = (low + high)//2
        maxRowInd = RowInd(mat,mid)
        left = mid-1
        if left>=0:
            left = mat[maxRowInd][mid-1]
        else:
            left=-1
        right = mid+1
        if right<m:
            right = mat[maxRowInd][mid+1]
        else:
            right = -1

        if mat[maxRowInd][mid]>left and mat[maxRowInd][mid]>right:
            return [maxRowInd,mid]
        elif mat[maxRowInd][mid]<left:
            high = mid-1
        else:
            low = mid+1
    return [-1,-1]

def main():
    mat = [[10,20,15],[21,30,14],[7,16,32]]
    print(findPeekInMat(mat))

main() 
        