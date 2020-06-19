def main(n):
    w, h = map(int, input().split())
    xy = [list(map(lambda x:int(x)-1, input().split())) for i in range(n)]
    s, t = map(int, input().split())
    field = [[0] * w for i in range(h)]
    for x, y in xy:
        field[y][x] = 1
    ans = 0
    for y in range(h - t + 1):
        for x in range(w - s + 1):
            b = 0
            for yi in range(t):
                for xi in range(s):
                    b += field[y + yi][x + xi]
            ans = max(ans, b)
    print(ans)
while 1:
    n = int(input())
    if n == 0:
        break
    main(n)