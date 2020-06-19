def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if not n % 2:
        return False
    for i in range(3, int(n ** 0.5) + 1,2):
        if n % i == 0:
            return False
    return True
def main(a, d, n):
    i = 0
    a -= d
    while i < n:
        a += d 
        if prime(a):
            i += 1
    print(a)
while 1:
    a, d, n = map(int, input().split())
    if a == d == n == 0:
        break
    main(a, d, n)