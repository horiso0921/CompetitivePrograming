from math import sqrt
def clc(xi, yi, xj, yj): return sqrt((xi - xj) ** 2 + (yi - yj) ** 2)
eps = 1e-5
def main(n):
    ans = 1
    ab = [[float(i) for i in input().split()]for _ in range(n)]
    full = [set([i]) for i in range(n)]
    for i in range(n):
        xi, yi = ab[i]
        for j in range(n):
            if i != j:
                xj, yj = ab[j]
                if 2 >= clc(xi, yi, xj, yj):
                    full[i].add(j)
    for i in range(n):
        xi, yi = ab[i]
        for j in range(i+1, n):
            xj, yj = ab[j]
            size = clc(xi, yi, xj, yj)
            if size > 2:
                continue
            cos = size / 2
            sin = sqrt(1 - cos ** 2)
            x = xj - xi
            y = yj - yi
            center1 = (xi + (cos * x - y * sin) / size,
                       yi + (x * sin + y * cos) / size)
            center2 = (xi + (cos * x + y * sin) / size,
                       yi + (- x * sin + y * cos) / size)
            tmp1 = 0
            tmp2 = 0
            for x in full[i] & full[j]:
                a, b = ab[x]
                if clc(center1[0], center1[1], a, b) <= 1 + eps:
                    tmp1 += 1
                if clc(center2[0], center2[1], a, b) <= 1 + eps:
                    tmp2 += 1
            tmp = max(tmp1, tmp2)
            if ans < tmp:
                ans = tmp
    print(ans)


if __name__ == "__main__":
    while 1:
        n = int(input())
        if n:
            main(n)
        else:
            break
