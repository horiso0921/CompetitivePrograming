S = list(input())
T = list(input())
alp = [chr(ord('a') + i) for i in range(26)]
al = [-1 for i in range(26)]
for i in range(len(S)):
    print(S[i],T[i])
    if al[alp.index(S[i])] == -1 and al[alp.index(T[i])] == -1:
        al[alp.index(S[i])] = alp.index(T[i])
        al[alp.index(T[i])] = alp.index(S[i])

        '''
    elif alp.index(T[i]) != al[alp.index(S[i])] and alp.index(S[i]) == -1:
        al[alp.index(S[i])] = alp.index(T[i])
    elif alp.index(T[i]) == -1 and alp.index(S[i]) != al[alp.index(T[i])]:
        al[alp.index(T[i])] = alp.index(S[i])
        '''
    else:
        if alp.index(T[i]) != al[alp.index(S[i])] or alp.index(S[i]) != al[alp.index(T[i])]:
            print("No")
            quit()
print("Yes")