def solve(n):
    i = 2
    while i**2 <= n:
        if n%i == 0:
            return 0
        i += 1
    return 1
while 1:
    n = int(input())
    if n == 0:
        break
    print(solve(n))
