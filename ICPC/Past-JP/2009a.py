def main(n, p):
    player = [0] * n
    ans = p
    while 1:
        for i in range(n):
            if p > 0:
                player[i] += 1
                p -= 1
                if p == 0 and player[i] == ans:
                    print(i)
                    return
            else:
                if player[i] > 0:
                    p += player[i]
                    player[i] = 0
while 1:
    n, p = map(int, input().split())
    if n == p == 0:
        break
    main(n,p)