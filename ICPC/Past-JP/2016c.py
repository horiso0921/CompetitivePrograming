def main(m, n):
    ck = [True] * (7368792)
    for i in range(m, 7368792):
        if ck[i]:
            n -= 1
            ck[i::i]=[False]*((7368791-i)//i+1)
            if n != 0:
                continue
            i += 1
            while not ck[i]:
                i += 1
            print(i)
            return
while 1:
    m, n = map(int, input().split())
    if n == m == 0:
        break
    main(m, n)

