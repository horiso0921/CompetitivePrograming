set = input()
set = set.split()
H = int(set[0])
W = int(set[1])
N = int(set[2])
field = []
for i in range(H):
	for j in range(W):
		field.append('.')
for i in range(N):
	n = 0
	lec = input()
	lec = lec.split()
	h = int(lec[0])
	w = int(lec[1])
	x = int(lec[2])
	for j in range(H):
		if (n == 0):
			for l in range(w):
				if (field[x+l+(j*W)] == "#"):
					n = 1
					bj = j
		if (n == 0):
			bj = j+1
	for k in range(h):
		for l in range(w):
			field[x+l+((bj-1-k)*W)] = "#"
for i in range(H):
	for j in range(W):
		print(field[j+(i*W)], end="")
	print()
				
	