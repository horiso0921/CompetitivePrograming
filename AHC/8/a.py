from collections import defaultdict, deque
from email.mime import base
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
from tkinter.messagebox import NO
from typing import Dict, List, Tuple
from random import randint

import sys
import itertools
import math

sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def S(): return input().rstrip()
def LS(): return S().split()
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]


MOD = 1000000007
INF = 1e10
OBST = 1
PET = 5
HUMAN = 3
VACANT = 2
ADJACENT = [(i, j) for i in range(-1, 2)
            for j in range(-1, 2) if i * j == 0 and i != j]
num_to_UDLR = {(0, -1): "L", (-1, 0): "U", (1, 0): "D", (0, 1): "R"}
UDLR_to_movement = {"U": (-1, 0), "D": (1, 0),
                    "L": (0, -1), "R": (0, 1), ".": (0, 0)}
num_to_udlr = {(0, -1): "l", (-1, 0): "u", (1, 0): "d", (0, 1): "r"}
udlr_to_movement = {"u": (-1, 0), "d": (1, 0),
                    "l": (0, -1), "r": (0, 1), ".": (0, 0)}

"""
目標：
1. x=15,y=15の全部に柵を設置 正し{(x, y):x∊{15}, y∊{14,15,16}には設置しない}
2. みんな(x,y)=(15,15)に集合
3. 一番ペットが少ない左右に所属できるように柵設置
3. 一番ペットが少ない上下に所属できるように柵設置
"""

FIRST_PHASE = "First"  # x=15,y=15の全部に柵を設置
SECOND_PHASE = "Second"  # みんな(x,y)=(15,15)に集合
THIRD_PHASE = "Third"  # 一番ペットが少ない上下に所属できるように柵設置
FOURTH_PHASE = "Fourth" # 一番ペットが少ない左右に所属できるように柵設置
FIFTH_PHASE = "Fifth" # 待機

NO_POSTER_NUM = 2

def solve():
    n = II()
    p = LIR_(n)
    m = II()
    h = LIR_(m)
    phase = [FIRST_PHASE]
    post_base = [30 // m]
    field = [[VACANT] * 30 for i in range(30)]

    for x, y, _ in p:
        field[x][y] *= PET
    for x, y in h:
        field[x][y] *= HUMAN

    def is_inside_field(x: int, y: int):
        return 0 <= x < 30 and 0 <= y < 30

    def can_post_phase():
        return phase[0] == FIRST_PHASE or phase[0] == THIRD_PHASE or phase[0] == FOURTH_PHASE

    def should_post_obst(x: int, y: int, index: int=0) -> bool:
        # print(f"#{x} {y}")
        if phase[0] == FIRST_PHASE:
            return (x == 15 and (y != 14 and y != 15 and y != 16)) or (y == 15 and x != 15)
        if phase[0] == THIRD_PHASE:
            return x == 15 and (y == 14 or y == 16)
        if phase[0] == FOURTH_PHASE:
            return abs(x - y) == 2 or x == y

    def can_post_obst(x: int, y: int, index: int) -> bool:
        if not is_inside_field(x, y):
            return False
        if not can_post_phase():
            return False
        if not should_post_obst(x, y, index):
            return False
        has_obj = field[x][y] % PET == 0 or field[x][y] % HUMAN == 0 or field[x][y] == OBST
        for mx, my in ADJACENT:
            mx += x
            my += y
            if is_inside_field(mx, my):
                has_obj |= field[mx][my] % PET == 0
        return not has_obj

    def can_move(x: int, y: int) -> bool:
        if not is_inside_field(x, y):
            return False
        return field[x][y] != OBST

    def has_obst(x: int, y: int):
        if not is_inside_field(x, y):
            return True
        return field[x][y] == OBST

    def change_phase():
        if phase[0] == FIRST_PHASE:
            for y in range(30):
                for x in range(30):
                    if should_post_obst(x, y):
                        if has_obst(x, y):
                            continue
                        else:
                            break
                else:
                    continue
                break
            else:
                phase[0] = SECOND_PHASE
        elif phase[0] == SECOND_PHASE:
            for i in range(NO_POSTER_NUM, m):
                x,y = h[i]
                if x == 15 and y == 15: continue
                break
            else:
                phase[0] = THIRD_PHASE
        elif phase[0] == THIRD_PHASE:
            if has_obst(15, 14) or has_obst(15, 16):
                phase[0] = FOURTH_PHASE
        elif phase[0] == FOURTH_PHASE:
            f = 0
            for i in [14, 16]:
                for j in [14, 16]:
                    if has_obst(i, j):
                        f = 1
            if f:
                phase[0] = FIFTH_PHASE

    def post_obst(x: int, y: int):
        print(f"#POST{x} {y}")
        field[x][y] = OBST

    def move_obj(move_dir_udlr: str, x: int, y: int, obj_type: int) -> Tuple[int, int]:
        move_x, move_y = x, y
        if move_dir_udlr in UDLR_to_movement:
            move_x, move_y = UDLR_to_movement[move_dir_udlr]
            move_y += y
            move_x += x
            field[x][y] //= obj_type
            field[move_x][move_y] *= obj_type
        return (move_x, move_y)

    def move_pet(s: List[str]):
        for i in range(n):
            x, y, c = p[i]
            for movement in s[i]:
                x, y = move_obj(movement, x, y, PET)
            p[i] = [x, y, c]
        return

    def move_human(s: Dict[int, str]):
        for i, movement in s.items():
            x, y = h[i]
            x, y = move_obj(movement, x, y, HUMAN)
            h[i] = [x, y]
        return

    def listup_move_human(post_human_list: List[int]) -> List[str]:
        cand = {i: 1 for i in range(m)}
        for i in post_human_list:
            cand[i] = 0
        res = []
        for k, v in cand.items():
            if v:
                res.append(k)
        return res

    def listup_obj_should_be_post() -> List[int]:
        res = []
        for x in range(30):
            for y in range(30):
                if should_post_obst(x, y) and field[x][y] != OBST:
                    res.append((x, y))
        return res
    
    def listup_box_should_be_moved(should_post: List[int]) -> List[int]:
        res = []
        for obj_box in should_post:
            x, y = obj_box
            for mx, my in ADJACENT:
                mx += x
                my += y
                if can_move(mx, my):
                    res.append((mx, my))
        return res
                    
    def search_way_from_now_to_distination(now_x: int, now_y: int, dist_x:int, dist_y:int) -> Tuple[int, int]:
        d = {}
        q = [[now_x+mx, now_y+my, (mx, my)] for mx, my in ADJACENT if can_move(now_x+mx, now_y+my)]
        # print(f"#{q}")
        for x,y,xy in q:
            d[(x,y)] = 1
            if x == dist_x and y == dist_y:
                return xy
        for xy in q:
            x,y,mxy = xy
            for mx, my in ADJACENT:
                mx += x
                my += y
                if can_move(mx, my) and not (mx, my) in d:
                    if mx == dist_x and my == dist_y:
                        return mxy
                    d[(mx, my)] = 1
                    nxy = [mx, my, mxy]
                    q.append(nxy)
        return None

    def decide_human_move(move_human_list: List[int]) -> Dict[int, str]:
        res = {}
        
        must_post = listup_obj_should_be_post()
        cand_box = listup_box_should_be_moved(must_post)
        print(f"#{phase}")
        # print(f"#{must_post}")
        # print(f"#{cand_box}")
        lis = [(0,0),(29,29),(0,29),(29,0)]

        for i in move_human_list:
            x,y = h[i]
            if 0 <= i < NO_POSTER_NUM:
                mx,my = lis[i]                
                way = search_way_from_now_to_distination(x, y, mx, my)
                if way == None:
                    res[i] = "."
                else:
                    res[i] = num_to_UDLR[way]
                continue
            if phase[0] == FIRST_PHASE:
                tmp = [500, (-1, -1)]
                for base_x, base_y in cand_box:
                    distance = abs(base_x - x) + abs(base_y - y)
                    if tmp[0] > distance:
                        tmp = [distance, (base_x, base_y)]
                base_x, base_y = tmp[1]
                way = search_way_from_now_to_distination(x, y, base_x, base_y)
                if way == None:
                    res[i] = "."
                else:
                    # print(f"#{way} {base_x} {base_y} {x} {y}")
                    res[i] = num_to_UDLR[way]
            elif phase[0] == SECOND_PHASE:
                base_x, base_y = 15,15
                if x == base_x and y == base_y:
                    res[i] = "."
                    continue
                way = search_way_from_now_to_distination(x, y, base_x, base_y)
                if way == None:
                    res[i] = "."
                else:
                    res[i] = num_to_UDLR[way]
            elif phase[0] == THIRD_PHASE:
                res[i] = "."
            elif phase[0] == FOURTH_PHASE:
                if has_obst(15, 14):
                    if can_move(x, y+1):
                        res[i] = "R"
                    else:
                        res[i] = "."
                elif can_move(x, y-1):
                    res[i] = "L"
                else:
                    res[i] = "."

            elif phase[0] == FIFTH_PHASE:
                res[i] = "."
            else:
                res[i] = "."

        return res

    def clc_range_pet(i: int, j: int, si: int, sj: int) -> int:
        c = [[1] * 30 for i in range(30)]
        c[i][j] = 0
        res = 0
        q = [(si, sj)]
        c[si][sj] = 0
        for x,y in q:
            f = field[x][y]
            while f % PET == 0:
                res += 1
                f //= PET
            for mxy in ADJACENT:
                mx, my = mxy
                mx += x
                my += y
                if can_move(mx, my) and c[mx][my]:
                    c[mx][my] = 0
                    q.append((mx, my))
        return res

    def decide_human_post(human_list: List[int]) -> Dict[int, str]:
        res = {}

        for i in human_list:
            x, y = h[i]
            if phase[0] == THIRD_PHASE:
                l_pet = clc_range_pet(x, y, x, y-1)
                r_pet = clc_range_pet(x, y, x, y+1)
                print(f"#{l_pet} {r_pet}")
                if l_pet > r_pet:
                    if can_post_obst(x, y-1, i):
                        post_obst(x, y-1)
                        res[i] = "l"
                else:
                    if can_post_obst(x, y+1, i):
                        post_obst(x, y+1)
                        res[i] = "r"
            elif phase[0] == FOURTH_PHASE:
                u_pet = clc_range_pet(x, y, x-1, y)
                d_pet = clc_range_pet(x, y, x+1, y)
                print(f"#{u_pet} {d_pet}, {can_post_obst(x+1, y, i)} {can_post_obst(x-1, y, i)}")
                if u_pet < d_pet:
                    if can_post_obst(x+1, y, i):
                        post_obst(x+1, y)
                        res[i] = "d"
                elif u_pet > d_pet: 
                    if can_post_obst(x-1, y, i):
                        post_obst(x-1, y)
                        res[i] = "u"
            else:
                for mxy in ADJACENT:
                    mx, my = mxy
                    mx += x
                    my += y
                    if is_inside_field(mx, my) and can_post_obst(mx, my, i):
                        post_obst(mx, my)
                        res[i] = num_to_udlr[mxy]
                        break

        return res

    def decide_human_movement() -> List[str]:
        post_human_dict = decide_human_post([i for i in range(NO_POSTER_NUM, m)])
        move_human_list = listup_move_human(list(post_human_dict.keys()))
        move_human_dict = decide_human_move(move_human_list)
        move_human(move_human_dict)
        change_phase()
        human_movement = []
        for i in range(m):
            if i in move_human_dict:
                human_movement.append(move_human_dict[i])
            else:
                human_movement.append(post_human_dict[i])
        return human_movement

    for i in range(300):
        movement = decide_human_movement()
        print("".join(movement), flush=True)

        move_pet(LS())
    return


# main
if __name__ == '__main__':
    solve()
