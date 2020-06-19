from collections import defaultdict
def main(n):
    S = list(input().split())
    d = defaultdict(int)
    d[0] = 0
    for num,s in enumerate(S):
        d[s] += 1
        di = sorted(d.items(), key=lambda x: x[1], reverse = True)
        if di[0][1] > di[1][1] + n - num - 1:
            print(di[0][0], num + 1)
            return
    print("TIE")
    return

while 1:
    n = int(input())
    if n == 0:
        break
    main(n)