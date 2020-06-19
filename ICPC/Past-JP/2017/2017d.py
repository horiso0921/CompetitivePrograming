from collections import defaultdict
def main(n, m):
    b = [int('0b' + input(), 0) for i in range(n)]
    ans = 0
    d = defaultdict(int)
    d[0] = 0
    for i in b:
        nd = defaultdict(int)
        for k, v in d.items():
            nd[k] = v
        for key, value in d.items():
            nd[key ^ i] = max(nd[key ^ i], value + 1)
        d = nd
    print(d[0])
    

if __name__ == "__main__":
    while 1:
        n,m = map(int, input().split())
        if n == 0: break
        main(n,m)