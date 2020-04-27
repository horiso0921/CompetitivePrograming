def II(): return int(input())


def LI(): return list(map(int, input().split()))

def LIR(n): return [LI() for _ in range(n)]
def S(): return input()


def solve():
    C = -1
    J = -1
    res = []
    n = II()
    se = LIR(n)
    se.sort()
    for start, end in se:
        if start >= C:
            res.append("C")
            C = end
        elif start >= J:
            res.append("J")
            J = end
        else:
            return "IMPOSSIBLE"
    return "".join(res)


if __name__ == '__main__':
    ans = []
    for _ in range(II()):
        ans.append(solve())
    for i, ai in enumerate(ans):
        print("Case #{}: {}".format(i+1, ai))
