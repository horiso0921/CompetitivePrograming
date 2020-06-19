def make(s1):
    i = 0
    l1 = []
    while i < len(s1):
        if s1[i] == '"':
            for k in range(i + 1, len(s1)):
                if s1[k] == '"':
                    l1.append((s1[i + 1:k], 1))
                    i = k + 1
                    break
        elif s1[i] == ";":
            for k in range(i, len(s1)):
                if s1[k] == ';':
                    l1.append((s1[i + 1:k],0))
                    i = k + 1
                    break
                if s1[k] == '"':
                    l1.append((s1[i + 1:k], 0))
                    i = k 
                    break
            else:
                l1.append((s1[i + 1:], 0))
                i = k + 1
        else:
            for k in range(i, len(s1)):
                if s1[k] == ';':
                    l1.append((s1[i:k], 0))
                    i = k + 1
                    break
                if s1[k] == '"':
                    l1.append((s1[i:k], 0))
                    i = k
                    break
            else:
                l1.append((s1[i:], 0))
                i = k + 1
    return l1

def main():
    s1 = input()
    s2 = input()
    l1 = make(s1)
    l2 = make(s2)
    if len(l1) != len(l2):
        print("DIFFERENT")
        return
    f = 0
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            if l1[i][1] == 0:
                f += 1
            f += 1
    if f == 0:
        print("IDENTICAL")
    elif f == 1:
        print("CLOSE")
    else:
        print("DIFFERENT")



for i in range(100):
    main()