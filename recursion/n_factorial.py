def factiorial(n):
    if n == 0:
        return 1
    # smaller_problem = factiorial(n-1)
    # biggerproblem = n*smaller_problem
    return n*factiorial(n-1)

n = int(input())
print("factorial of ",n," is:",factiorial(n))