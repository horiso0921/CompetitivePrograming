E = list(map(int, input().split()))
B = int(input())
L = list(map(int, input().split()))
ans = 0
ansl = [0,0,0,5,4,3,1]
for i in range(6):
    if E[i] in L:
        ans += 1

if ans == 5:
    if B in L:
        print(2)
    else:
        print(3)
else:
    print(ansl[ans])