def main(n):
    a = list(map(int, input().split()))
    a.sort()
    ans = 10 ** 20
    for i in range(n - 1):
        if ans > a[i + 1] - a[i]:
            ans = a[i + 1] - a[i]
    print(ans)

while 1:
    n = int(input())
    if n == 0:
        break
    main(n)