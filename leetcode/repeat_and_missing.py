matrix = [1,3,5,4,4]
n = len(matrix)
SN = (n * (1 + n)) // 2
S2N = (n * (n + 1) * (2 * n + 1)) // 6

s, s2 = 0, 0

for i in range(n):
    s += matrix[i]
    s2 += matrix[i] * matrix[i]
val1 = s - SN
val2 = s2 - S2N
val2 = val2 // val1
x = (val1 + val2) // 2
y = x - val1

print([x,y])