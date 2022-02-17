from collections import defaultdict, deque
from email.mime import base
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
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

FIRST_PHASE = "First"  # 上に並ぶ
SECOND_PHASE = "Second"  # 縦に並べる
THIRD_PHASE = "Third"  # 中央に向かう
FOURTH_PHASE = "Fourth"  # 中央に並べる
FIFTH_PHASE = "FIFTH"  # 最後の一個を置く位置に行く
SIXTH_PHASE = "SIXTH"  # 最後の一個を置く


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
        return phase[0] == SECOND_PHASE or phase[0] == FOURTH_PHASE or phase[0] == SIXTH_PHASE

    def should_post_obst(x: int, y: int, index: int) -> bool:
        if phase[0] == SECOND_PHASE:
            return y == index * post_base[0]
        if phase[0] == FOURTH_PHASE:
            res = x == 15
            if has_obst(x, y + 1) and has_obst(x, y - 1):
                res &= False
            return res
        if phase[0] == SIXTH_PHASE:
            return x == 14 or x == 16

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
            for i in range(1, m):
                x, y = h[i]
                if x == 0 and abs(y - post_base[0] * i) == 1:
                    continue
                print(f"#{x}{y}")
                break
            else:
                phase[0] = SECOND_PHASE
        elif phase[0] == SECOND_PHASE:
            for i in range(1, m):
                for j in range(30):
                    if has_obst(j, post_base[0] * i):
                        continue
                    break
                else:
                    continue
                break
            else:
                phase[0] = THIRD_PHASE
        elif phase[0] == THIRD_PHASE:
            for i in range(1, m):
                x, y = h[i]
                if abs(x - 15) == 1:
                    continue
                print(f"#{x}{y}")
                break
            else:
                phase[0] = FOURTH_PHASE
        elif phase[0] == FOURTH_PHASE:
            for i in range(1, m):
                x, y = h[i]
                if has_obst(x + 1, y) or has_obst(x - 1, y):
                    break
                if has_obst(x+1, y + 1) and has_obst(x+1, y - 1) or has_obst(x-1, y + 1) and has_obst(x-1, y - 1):
                    continue
                break
            else:
                phase[0] = FIFTH_PHASE
        elif phase[0] == FIFTH_PHASE:
            for i in range(1, m):
                x, y = h[i]
                if has_obst(x , y-1) or has_obst(x, y+1):
                    continue
                break
            else:
                phase[0] = SIXTH_PHASE


    def post_obst(x: int, y: int):
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
            if field[x][15] != OBST:
                res.append(x)
        return res

    def decide_human_move(move_human_list: List[int]) -> Dict[int, str]:
        res = {}
        print(f"#{phase}")

        for i in move_human_list:
            x, y = h[i]
            if i == 0:
                mx, my = ADJACENT[1]
                if can_move(x+mx, y+my):
                    res[i] = num_to_UDLR[(mx, my)]
                else:
                    res[i] = "."
            else:
                if phase[0] == FIRST_PHASE:
                    base_y = post_base[0] * i
                    base_x = 0
                    if abs(y - base_y) != 1:
                        if y > base_y:
                            res[i] = "L"
                        else:
                            res[i] = "R"
                    elif x != base_x:
                        if x > base_x:
                            res[i] = "U"
                    else:
                        res[i] = "."
                elif phase[0] == SECOND_PHASE:
                    for mx, my in ADJACENT:
                        mx += x
                        my += y
                        if is_inside_field(mx, my) and should_post_obst(mx, my, i) and has_obst(mx, my):
                            if can_move(x+1, y):
                                res[i] = "D"
                            else:
                                res[i] = "."
                            break
                    else:
                        res[i] = "."
                elif phase[0] == THIRD_PHASE:
                    base_x = 15
                    if abs(base_x - x) != 1:
                        if x > base_x:
                            res[i] = "U"
                        else:
                            res[i] = "D"
                    else:
                        res[i] = "."
                elif phase[0] == FOURTH_PHASE:
                    base_y = post_base[0] * i
                    for mx, my in ADJACENT:
                        mx += x
                        my += y
                        if is_inside_field(mx, my) and should_post_obst(mx, my, i) and has_obst(mx, my):
                            if y > base_y:
                                if can_move(x, y+1):
                                    res[i] = "R"
                                    break
                            else:
                                if can_move(x, y-1):
                                    res[i] = "L"
                                    break
                    else:
                        res[i] = "."
                elif phase[0] == FIFTH_PHASE:
                    base_y = post_base[0] * i
                    base_x = 15
                    if x > base_x:
                        if can_move(x-1, y):
                            res[i] = "U"
                            continue
                    elif x < base_x:
                        if can_move(x+1, y):
                            res[i] = "D"
                            continue
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
            if phase[0] == SIXTH_PHASE:
                if has_obst(x-1, y) or has_obst(x+1, y): continue
                u_pet = clc_range_pet(x, y, x-1, y)
                d_pet = clc_range_pet(x, y, x+1, y)
                print(f"#{u_pet} {d_pet}")
                if u_pet < d_pet:
                    if can_post_obst(x+1, y, i):
                        post_obst(x+1, y)
                        res[i] = "d"
                else:
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
        post_human_dict = decide_human_post([i for i in range(1, m)])
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
