check = [True]*(3*10**5+1)
pri = []
for i in range(6,3 * 10 ** 5 + 1):
    if (i % 7 == 1 or i % 7 == 6) and check[i]:
        pri.append(i)
        for k in range(i * 2, 3 * 10 ** 5 + 1, i):
            check[k] = False

def main(n):
    res = ["{}:".format(n)]
    for p in pri:
        if n % p == 0:
            res.append(str(p))
    print(" ".join(res))
while 1:
    n = int(input())
    if n == 1:
        break
    main(n)