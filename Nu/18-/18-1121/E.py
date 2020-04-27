S = input()
for i in range(len(S)):
    if S[i] == "O":
        print("0", end="")
    elif S[i] == "D":
        print("0", end="")
    elif S[i] == "I":
        print("1", end="")
    elif S[i] == "Z":
        print("2", end="")
    elif S[i] == "S":
        print("5", end="")
    elif S[i] == "B":
        print("8", end="")
    else:
        print(S[i], end="")
print("")