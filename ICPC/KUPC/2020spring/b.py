h,w = map(int, input().split())
s = [input() for i in range(h)]
gt0 = "6314"*25
gt4 = "1364"*25
gt1 = "2#"*50
gt2 = "5#"*50
gt = [None] * 100
for y in range(100):
    if y & 1:
        if y & 2:
            gt[y] = gt2
        else:
            gt[y] = gt1
    else:
        if y & 2:
            gt[y] = gt4
        else:
            gt[y] = gt0

field = [[True] * 100 for i in range(100)]
field[0][0] = False

q = [(0,0)]
move = [(0,1),(1,0),(0,-1),(-1,0)]

while q:
    x,y = q.pop()
    for mx, my in move:
        mx+=x
        my+=y
        if 0 <= mx < w and 0 <= my < h:
            if field[my][mx] and gt[my][mx] != "#" and gt[my][mx] == s[my][mx]:
                field[my][mx] = False
                q.append((mx, my))
h,w = map(int, input().split())
s = [input() for i in range(h)]
gt0 = "6314"*25
gt4 = "1364"*25
gt1 = "2#"*50
gt2 = "5#"*50
gt = [None] * 100
for y in range(100):
    if y & 1:
        if y & 2:
            gt[y] = gt2
        else:
            gt[y] = gt1
    else:
        if y & 2:
            gt[y] = gt4
        else:
            gt[y] = gt0

field = [[True] * 100 for i in range(100)]
field[0][0] = False

q = [(0,0)]
move = [(0,1),(1,0),(0,-1),(-1,0)]

while q:
    x,y = q.pop()
    for mx, my in move:
        mx+=x
        my+=y
        if 0 <= mx < w and 0 <= my < h:
            if field[my][mx] and gt[my][mx] != "#" and gt[my][mx] == s[my][mx]:
                field[my][mx] = False
                q.append((mx, my))


if not field[h-1][w-1]:
    print('YES')
else:
    print('NO')

if not field[h-1][w-1]:
    print('YES')
else:
    print('NO')