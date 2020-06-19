def prime(n):
    for i in range(2,int((n)**0.5)+1):
        if n % i == 0:
            return False
    return True

def main(n):
    ans = 0
    for i in range(n+1,2*n+1):
        if prime(i):
            ans += 1
    print(ans)
while 1:
    n = int(input())
    if n == 0:
        break
    main(n)