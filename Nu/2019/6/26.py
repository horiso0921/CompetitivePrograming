def main_a():
    y, m, d = map(int, input().split())
    a = (y - 1) // 3
    b = (y - 1) % 3
    c = a * 590 + 195 * b 
    if y % 3:
        a = (m - 1) // 2
        b = (m - 1) % 2
        c += a * 39 + b * 20
    else:
        c += (m - 1) * 20
    c += d - 1
    print(196470 - c)
def a():
    n = int(input())
    for _ in range(n):
        main_a()

def main_b():
    s = input()
    ans = []
    for i in range(1,len(s)):
        ans.append(s[:i] + s[i:])
        ans.append(s[i-1::-1] + s[i:])
        ans.append(s[i-1::-1] + s[len(s):i-1:-1])
        ans.append(s[:i] + s[len(s):i - 1:-1])
        ans.append(s[i:] + s[:i])
        ans.append(s[i:] + s[i - 1::-1])
        ans.append(s[len(s):i - 1:-1] + s[i - 1::-1])
        ans.append(s[len(s):i - 1:-1] + s[:i])
    print(len(set(ans)))

def b():
    n = int(input())
    for _ in range(n):
        main_b()

def main_c(n, m):
    a = [0] * n
    s = [0] * n
    for _ in range(m):
        skc = list(map(int, input().split()))
        si = skc[0]
        c = skc[2:]
        if skc[1] == 1:
            s[c[0] - 1] += si
        for i in c:
            a[i-1] += si
    an = max(a)
    anindex = a.index(an)

    sm = 10**20
    for i in range(n):
        if i != anindex:
            if sm > s[i]:
                sm = s[i]

    flg = False
 
    for i in range(n):
        if i != anindex:
            if s[i] == 0:
                flg = True
    if flg:
        ans = an + 1
    else:
        ans = an + 1 - sm
    print(ans)


def c():
    while 1:
        n, m = map(int, input().split())
        if n == m == 0:
            return
        main_c(n,m)

c()

