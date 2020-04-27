def main(M, T, P, R):
    team = [[0, 0, i + 1] for i in range(T)]
    teamprob = [[0] * P for i in range(T)]
    for _ in range(R):
        m, t, p, r = map(int, input().split())
        if r == 0:
            team[t - 1][0] += 1
            team[t - 1][1] -= m
            team[t - 1][1] -= teamprob[t - 1][p - 1]
        else:
            teamprob[t - 1][p - 1] += 20
    team.sort(reverse=True)
    ans = "{0}".format(team[0][2])
    for i in range(1,T):
        if team[i - 1][0] == team[i][0]:
            if team[i - 1][1] == team[i][1]:
                ans += "="
            else:
                ans += ","
        else:
            ans += ","
        ans += "{0}".format(team[i][2])
    print(ans)

while 1:
    m, t, p, r = map(int, input().split())
    if m == t == p == r == 0:
        break
    main(m, t, p, r)