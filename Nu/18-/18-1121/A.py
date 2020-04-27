S = input()
al = [chr(i) for i in range(97, 97+26)]
S = set(S)
al = set(al)
A = al - S
A = list(A)
A.sort()
if len(A) == 0:
    print("None")
else:
    print(A[0])