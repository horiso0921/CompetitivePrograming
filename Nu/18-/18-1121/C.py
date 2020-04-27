A= list(map(int, input().split()))
A.sort()

ANS = A[2] - A[1]
A[0] +=  A[2] - A[1]
if (A[2] - A[0]) % 2 == 0:
    ANS += (A[2] - A[0])//2
    print(ANS)
else:
    ANS += (A[2] - A[0]+1)//2
    print(ANS+1)