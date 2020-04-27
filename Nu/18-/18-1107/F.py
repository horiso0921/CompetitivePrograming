import string
CH = [chr(i) for i in range(65, 65+26)]
ANS = [0 for i in range(26)]
ANSB = [100 for i in range(26)]
N = int(input())
A = list(input())
B = list(input())
for i in range(N):
    if(i == 0):
        if(str.isdigit(A[i]) and str.isdigit(B[i])):
            continue
        elif(str.isdigit(A[i]) and str.isalpha(B[i])):
            ANS[CH.index(B[i])] = 1
        elif(str.isdigit(B[i]) and str.isalpha(A[i])):
            ANS[CH.index(A[i])] = 1
        elif(str.isalpha(A[i]) and str.isalpha(B[i])):
            ANS[CH.index(A[i])] = 9
            ANS[CH.index(B[i])] = 9
            ANSB[CH.index(A[i])] = CH.index(B[i])
            ANSB[CH.index(B[i])] = CH.index(A[i])
    else:
        if(str.isdigit(A[i]) and str.isdigit(B[i])):
            continue
        elif(str.isdigit(A[i]) and str.isalpha(B[i])):
            ANS[CH.index(B[i])] = 1
            if(ANSB[CH.index(B[i])] != 100):
                ANS[ANSB[CH.index(B[i])]] = 1
        elif(str.isdigit(B[i]) and str.isalpha(A[i])):
            ANS[CH.index(A[i])] = 1
        elif(str.isalpha(A[i]) and str.isalpha(B[i])):
            if(ANS[CH.index(A[i])] == 1 and ANS[CH.index(B[i])] == 1):
                continue
            elif(ANS[CH.index(A[i])] == 1 and ANS[CH.index(B[i])] == 0):
                ANS[CH.index(B[i])] = 1
            elif(ANS[CH.index(B[i])] == 1 and ANS[CH.index(A[i])] == 0):
                ANS[CH.index([i])] = 1
            elif(ANS[CH.index(A[i])] == 0 and ANS[CH.index(B[i])] == 0):
                ANS[CH.index(A[i])] = 10
                ANS[CH.index(B[i])] = 10
ans = 1
for i in range(26):
    if(ANS[i] != 0):
        ans *= ANS[i]

print(ans)