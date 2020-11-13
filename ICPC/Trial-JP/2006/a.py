def main():
    n = int(input())
    if n == 0: return False
    d = set()
    N = n
    for _ in range(n):
        a,b = map(int, input().split())
        d.add((a,b))
    now = [10,10]
    mo = {"N": (0,1), "E": (1,0), "S": (0,-1), "W": (-1,0)}
    for i in range(int(input())):
        n,m = input().split()
        m = int(m)
        mx,my = mo[n]
        for _ in range(m):
            now[0] += mx
            now[1] += my
            if (now[0], now[1]) in d:
                d.remove((now[0], now[1]))
    if d:
        print("No")
    else:
        print("Yes")
    return True

while main():
    pass
