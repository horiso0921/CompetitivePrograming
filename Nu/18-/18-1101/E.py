N,A,B = map(int, input().split())
C = A + B 
while (1):
    if(N-C > 0):
        N -= C
    else:
        if(N-A<=0):
            print("Ant")
            break
        else:
            print("Bug")
            break