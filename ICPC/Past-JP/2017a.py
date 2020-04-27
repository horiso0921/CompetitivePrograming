import itertools
def main(n,m):
    a = list(map(int, input().split()))
    select = list(itertools.combinations(range(n), 2))
    ans = 0
    for x,y in select:
        if ans < a[x] + a[y] <= m:
            ans = a[x] + a[y]
    if ans == 0:
        print("NONE")
    else:
        print(ans)
    return 1
while 1:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    main(n,m)