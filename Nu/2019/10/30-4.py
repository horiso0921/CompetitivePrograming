def main(n, m, q):
    ans = [set() for i in range(m)]
    sb = [["0" * n, "0" * m]] + [input().split() for i in range(q)]
    print(sb)
    for i in range(m):
        for k in range(n):
            ans[i].add(k)
    for i in range(m):
        for k in range(q):
            if sb[k + 1][1][i] != sb[k][1][i]:
                tmp = set()
                for l in range(n):
                    if sb[k + 1][0][l] == "1":
                        tmp.add(l)
                print(tmp)
                ans[i] = ans[i] & tmp
    for i in ans:
        print(i)
        if len(i) == 1:
            print(i[0], end="")
        else:
            print("?", end="")
    print()




if __name__ == "__main__":
    while 1:
        n, m, q = map(int, input().split())
        if n == m == q == 0:
            break
        main(n, m, q)