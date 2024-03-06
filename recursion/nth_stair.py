
def nthStair(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    ans = nthStair(n-1) + nthStair(n-2)
    return ans

n = int(input())
print("nth stair to count is:",nthStair(n))