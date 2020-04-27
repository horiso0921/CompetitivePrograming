from collections import defaultdict
inf = float("INF")
binary = [1 << i for i in range(14)]

def main(n):

    s = [input() for _ in range(n)]
    delete = set()
    for i in range(n):
        for k in range(n):
            if i == k:
                continue
            if s[k] in s[i]:
                delete.add(k)
    n -= len(delete)
    for de in reversed(sorted(delete)):
        del s[de]

    mindist = [[inf] * n for _ in range(n)]
    lenlis = [len(s[i]) for i in range(n)]
    for i in range(n):
        mindisti = mindist[i]
        si = s[i]
        for k in range(n):
            if i == k:
                continue
            sk = s[k]
            lenk = lenlis[k]
            if sk in si:
                tmp = 0
            else:
                tmp = lenk
                for index_k in range(1, lenk + 1):
                    if sk[:index_k] == si[-index_k:]:
                        tmp = lenk - index_k
            mindisti[k] = tmp

    d = defaultdict(int)
    for i in range(n):
        d[(binary[i], i)] = len(s[i])

    for _ in range(n-1):
        nd = defaultdict(lambda: inf)
        for key, value in d.items():
            state, before = key
            mindistb = mindist[before]

            for i in range(n):
                if not (state >> i & 1):
                    if nd[(state ^ binary[i], i)] > value + mindistb[i]:
                        nd[(state ^ binary[i], i)] = value + mindistb[i]

        d = nd

    print(min(d.values()))


if __name__ == "__main__":
    while 1:
        n = int(input())
        if n:
            main(n)
        else:
            break