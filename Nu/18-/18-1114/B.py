A, B =map(int, input().split())
S = input()
NUM = list(range(10))
X = 0
while X != A+B+1:
    if X == A:
        if S[X] != "-":
            print("No")
            quit()
        X += 1
    else:
        if S[X] == "-":
            print("No")
            quit()
        if int(S[X]) in NUM:
            X += 1
        else:
            print("No")
            quit()
print("Yes")