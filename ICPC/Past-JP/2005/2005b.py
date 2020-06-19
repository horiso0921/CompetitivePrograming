def check(a, b):
    for _ in range(4):
        if a == b:
           return True
        b = list(map(lambda x: [-x[1], x[0]], b))
    return False


def main(n):
    lines = [None] * n
    for i in range(n):
        m = int(input())
        xy = [None] * m
        for j in range(m):
            xy[j] = list(map(int, input().split()))
        lines[i] = xy
    x, y = lines[0][0]
    ans = list(map(lambda z: [z[0] - x, z[1] - y], lines[0]))
    for num, line in enumerate(lines[1:]):
        x, y = line[0]
        fline = list(map(lambda z: [z[0] - x, z[1] - y], line))
        x, y = line[-1]
        eline = list(map(lambda z: [z[0] - x, z[1] - y], line[::-1]))
        if check(ans, fline) or check(ans, eline):
            print(num+1)
    print("+" * 5)



while 1:
    n = int(input())
    if n == 0:
        break
    main(n + 1)