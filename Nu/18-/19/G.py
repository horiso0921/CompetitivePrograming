s = input()

for i in range(len(s)-3):
    if s[i] == s[i + 1]:
        print(i)
        if s[i + 1] == s[i + 2]:
            print(i + 1, i + 3)
            quit()
        elif s[i + 1] != s[i + 2] and s[i + 3] == s[i]:
            print(i+1, i + 4)
            quit()
print(-1,-1)
        