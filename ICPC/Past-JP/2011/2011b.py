def main(s):
    s = "".join(list(s.split()))
    bra1 = 0
    bra2 = 0
    for i in range(len(s)):
        if s[i] != "(" and s[i] != ")" and s[i] != "[" and s[i] != "]":
            continue
        if s[i] == "(":
            if bra1 == 0:
                bra10 = i
            bra1 += 1
        if s[i] == ")":
            bra1 -= 1
            if bra1 == 0:
                if not main(s[bra10 + 1:i]):
                    return False
        if s[i] == "[":
            if bra2 == 0:
                bra20 = i
            bra2 += 1
        if s[i] == "]":
            bra2 -= 1
            if bra2 == 0:
                if not main(s[bra20 + 1:i]):
                    return False
        if bra1 < 0 or bra2 < 0:
            return False
    if bra1 > 0 or bra2 > 0:
        return False
    return True

while 1:
    s = input()
    if s == ".":
        break
    print("yes" if main(s) else "no")
    