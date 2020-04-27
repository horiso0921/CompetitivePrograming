def main(n, m, p, a, b):
    t = list(map(int, input().split()))
    p = t

while 1:
    n, m, p, a, b = map(int, input().split())
    if n == m == p == a == b == 0:
        break
    main(n, m, p, a, b)