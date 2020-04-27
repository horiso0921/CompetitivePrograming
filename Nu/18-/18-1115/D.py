A, B = map(int, input().split())
ANS = ["Ant","Bug","Draw"]
if abs(A) > abs(B):
    print(ANS[1])
elif abs(A) < abs(B):
    print(ANS[0])
else:
    print(ANS[2])