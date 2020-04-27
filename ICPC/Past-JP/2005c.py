def S(s):
    m = ["i", "x", "c", "m"]
    res = 0
    i = 0
    tmp = 1
    while i < len(s):
        if "2" <= s[i] <= "9":
            tmp = int(s[i])
        else:
            res += tmp * 10 ** m.index(s[i])
            tmp = 1
        i += 1
    return res
def main():
    m1 = ["i", "x", "c", "m"]
    s1, s2 = list(map(str, input().split()))
    ms1 = S(s1)
    ms2 = S(s2)
    ms = ms1 + ms2
    m = str(ms)
    m = m[::-1]
    res = ""
    for i in range(len(m)):
        if m[i] == "0":
            continue
        if m[i] == "1":
            res = m1[i] + res
            continue
        res = m[i] + m1[i] + res
    print(res)


n = int(input())
for _ in range(n):
    main()