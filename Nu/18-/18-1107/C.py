X, Y = map(int, input().split())
score = 1
A = X
while 1:
    A *= 2
    if(A <= Y):
        score += 1
    else:
        print(score)
        break