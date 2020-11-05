n = int(input())
ans = []
for _ in range(n):
    s = input()
    for si in s:
        if "A" <= si <= "Z":
            ans.append(si)
print("".join(ans+["U", "P", "C"]))