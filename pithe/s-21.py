play = input()
play = play.split()
N = int(play[0])
M = int(play[1])
P = int(play[2])
mons = []
ti = []
ai = []
ci = []
for i in range(N):
	hp = int(input())
	mons.append(hp)
for i in range(M):
	mg = input()
	mg = mg.split()
	t = mg[0]
	a = int(mg[1])
	c = int(mg[2])
	ti.append(t)
	ai.append(a)
	ci.append(c)
