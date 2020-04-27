import sys
N = list(input())
M = list(input())

N.sort()
M.sort(reverse = True)

if(len(N) < len(M)):
    for i in range(len(N)):
        if(M[i] > N[i]):
            print("Yes")
            sys.exit()
        elif(M[i] == N[i]):
            continue
        else:
            print("No")
            sys.exit()
    print("Yes")

if(len(N) >= len(M)):
    for i in range(len(M)):
        if(M[i] > N[i]):
            print("Yes")
            sys.exit()
        elif(M[i] == N[i]):
            continue
        else:
            print("No")
            sys.exit()
    print("No")
