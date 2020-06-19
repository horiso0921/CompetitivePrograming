import bisect
def main(n):
    a = list(map(int, input().split()))
    a.sort()
    print(bisect.bisect_right(a,sum(a)/n))

while 1:
    n = int(input())
    if n == 0:
        break
    main(n)