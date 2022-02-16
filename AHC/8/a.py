from collections import defaultdict, deque
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


def solve():
    n = II()
    p = LIR_(n)
    m = II()
    h = LIR_(m)
    poster = m - 4
    field = [[VACANT] * 30 for i in range(30)]

    for x, y, _ in p:
        field[x][y] *= PET
    for x, y in h:
        field[x][y] *= HUMAN

    def is_inside_field(x: int, y: int):
        return 0 <= x < 30 and 0 <= y < 30

    def can_post_obst(x: int, y: int, normal=True) -> bool:
        if not is_inside_field(x, y):
            return False
        if normal and y != 15:
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
        yet_post = listup_obj_should_be_post()
        for i in move_human_list:

            if poster <= i < m:
                mx, my = ADJACENT[randint(0, 3)]
                x, y = h[i]
                if can_move(x+mx, y+my):
                    print(f"#{mx} {x} {y} {my}{num_to_UDLR[(mx,my)]}")
                    res[i] = num_to_UDLR[(mx, my)]
                else:
                    res[i] = "."
            else:
                if len(yet_post) == 1:
                    cand = yet_post[0]
                    x, y = h[i]
                    if x == cand and y == 15:
                        res[i] = "."
                    else:
                        if x == cand:
                            if y >= 16:
                                res[i] = "L"
                                continue
                            else:
                                res[i] = "R"
                                continue
                        if x < cand:
                            res[i] = "D"
                        else:
                            res[i] = "U"
                else:
                    x, y = h[i]
                    print(f"#{x}{y}{res}")
                    if y == 15:
                        res[i] = "L"
                        continue
                    if y > 16:
                        res[i] = "L"
                        continue
                    if y < 14:
                        res[i] = "R"
                        continue
                    tmp = [-1, INF]
                    for post_cand in yet_post:
                        distance = abs(y - 15) + abs(x - post_cand)
                        if distance < tmp[-1]:
                            tmp = [post_cand, distance]
                    print(f"#{tmp}")
                    if tmp[-1] == INF:
                        res[i] = "."
                    elif tmp[-1] != 1:
                        if tmp[0] > x:
                            res[i] = "D"
                        elif tmp[0] < x:
                            res[i] = "U"
                    else:
                        res[i] = "."

        print(f"#{res}{yet_post}{move_human_list}")
        return res

    def decide_obst_post(human_list: List[int]) -> Dict[int, str]:
        yet_post = listup_obj_should_be_post()
        res = {}
        print(f"#{human_list}{h}")
        # for fi in field:
        #     print(f"#{fi}")
        if len(yet_post) == 1:
            for i in range(poster):
                x, y = h[i]
                if x == yet_post[0] and y == 15:
                    continue
                break
            else:
                cand = yet_post[0]
                l_pet = 0
                r_pet = 0
                for x in range(30):
                    for y in range(15):
                        f = field[x][y]
                        while f % PET == 0:
                            f //= PET
                            l_pet += 1

                for x in range(30):
                    for y in range(15, 30):
                        f = field[x][y]
                        while f % PET == 0:
                            f //= PET
                            r_pet += 1

                if l_pet >= r_pet:
                    if can_post_obst(cand, 14, False):
                        res[0] = "l"
                        post_obst(cand, 14)
                        human_list.remove(0)
                elif r_pet < l_pet:
                    if can_post_obst(cand, 16, False):
                        res[0] = "r"
                        post_obst(cand, 16)
                        human_list.remove(0)

        for i in human_list:
            x, y = h[i]
            for mxy in ADJACENT:
                mx, my = mxy
                mx += x
                my += y
                if is_inside_field(mx, my) and can_post_obst(mx, my):
                    post_obst(mx, my)
                    res[i] = num_to_udlr[mxy]
                    break

        return res

    def decide_human_movement() -> List[str]:
        post_human_dict = decide_obst_post([i for i in range(poster)])
        move_human_list = listup_move_human(list(post_human_dict.keys()))
        move_human_dict = decide_human_move(move_human_list)
        move_human(move_human_dict)
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
