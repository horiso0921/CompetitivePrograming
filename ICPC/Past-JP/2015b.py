checklis = [5,7,5,7,7]
def check(S):
    b = 0
    index = 0
    for s in S:
        b += len(s)
        if checklis[index] == b:
            index += 1
            b = 0
            if index == 5:
                return True
        elif checklis[index] > b:
            continue
        else:
            return False
    return False

def main(n):
    s = [input() for i in range(n)]
    for i in range(n):
        if check(s[i:]):
            print(i + 1)
            return

while 1:
    n = int(input())
    if n == 0:
        break
    main(n)