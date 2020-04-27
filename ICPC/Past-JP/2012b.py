def Numseque(a, l):
    a = list(str(a))
    while len(a) < l:
        a.insert(0,"0")
    a.sort()
    a0 = a
    a0 = "".join(a0)
    a.sort(reverse=True)
    a1 = a
    return int("".join(a1))-int(a0)

def main(a0, l):
    a = [a0]
    while 1:
        a.append(Numseque(a[-1], l))
        if a[-1] in a[:len(a) - 1]:
            for i in range(len(a)):
                if a[-1] == a[i]:
                    j = i
                    break
            print(j, a[-1], len(a)-1-j)
            return 


while 1:
    a, l = map(int, input().split())
    if a == l == 0:
        break
    main(a,l)