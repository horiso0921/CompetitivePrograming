def main():
    from collections import defaultdict
    n = int(input())
    u = [input() for i in range(n)]
    d = defaultdict(int)
    for ui in u:
        d[ui] = 1
    m = int(input())
    f = True
    for _ in range(m):
        n = input()
        if d[n]:
            if f:
                print("Opened by " + n)
                f ^= 1
            else:
                print("Closed by " + n)
                f ^= 1
        else:
            print("Unknown " + n)

if __name__ == "__main__":
    main()