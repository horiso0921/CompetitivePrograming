A, B = map(int, input().split())
S = input()
NUM = [str(i) for i in range(10)]

for i in range(A):
    if S[i] not in NUM:
        print("No")
        quit()

if S[A] != "-":
    print("No")
    quit()

for i in range(A + 1, A+B+1):
    if S[i] not in NUM:
        print("No")
        quit()
print("Yes")       