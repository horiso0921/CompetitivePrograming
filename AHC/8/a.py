from collections import defaultdict, deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
from typing import Dict, List, Tuple

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
num_to_UDLR = {(-1, 0): "L", (0, -1): "U", (0, 1): "D", (1, 0): "R"}
UDLR_to_movement = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0), ".": (0, 0)}
num_to_udlr = {(-1, 0): "l", (0, -1): "u", (0, 1): "d", (1, 0): "r"}
udlr_to_movement = {"u": (0, -1), "d": (0, 1), "l": (-1, 0), "r": (1, 0), ".": (0, 0)}


def solve():
    n = II()
    p = LIR_(n)
    m = II()
    h = LIR_(m)
    field = [[VACANT] * 30 for i in range(30)]
    for x, y, _ in p:
        field[y][x] *= PET
    for x, y in h:
        field[y][x] *= HUMAN

    def is_inside_field(y: int, x: int):
        return 0 <= y < 30 and 0 <= x < 30

    def can_post_obst(y: int, x: int) -> bool:
        if not is_inside_field(y, x):
            return False
        has_obj = field[y][x] % PET == 0 or field[y][x] % HUMAN == 0 or field[y][x] == OBST
        for my, mx in ADJACENT:
            my += y
            mx += x
            if is_inside_field(my, mx):
                has_obj |= field[my][mx] % PET == 0 or field[y][x] == OBST
        return not has_obj

    def can_move(y: int, x: int) -> bool:
        if not is_inside_field(y, x):
            return False
        return field[y][x] != OBST
    
    def post_obst(y: int, x: int):
        field[y][x] = OBST

    def move_obj(move_dir_udlr: str, y: int, x: int, obj_type: int) -> Tuple[int, int]:
        move_y, move_x = UDLR_to_movement[move_dir_udlr]
        move_y += y
        move_x += x
        field[y][x] //= obj_type
        field[move_y][move_x] *= obj_type
        return (move_y, move_x)

    def move_pet(s: List[str]):
        for i in range(n):
            x, y, c = p[i]
            for movement in s[i]:
                y, x = move_obj(movement, y, x, PET)
            p[i] = [x, y, c]
        return

    def move_human(s: Dict[int, str]):
        for i, movement in s.items():
            x, y = h[i]
            y, x = move_obj(movement, y, x, HUMAN)
            h[i] = [x, y]
        return

    def decide_human_move() -> Dict[int, str]:
        return {}

    def listup_obst_post_human(movement_human_list: List[int]) -> List[str]:
        cand = {i: 1 for i in range(m)}
        for i in movement_human_list:
            cand[i] = 0
        res = []
        for k, v in cand.items():
            if v:
                res.append(k)
        return res

    def decide_obst_post(human_list: List[int]) -> Dict[int, str]:
        res = {}
        for i in human_list:
            x, y = h[i]
            for myx in ADJACENT:
                my, mx = myx
                my += y
                mx += x
                if is_inside_field(my, mx) and can_post_obst(my, mx):
                    post_obst(my, mx)
                    res[i] = num_to_udlr[myx]
                    break
            else:
                res[i] = "."
        return res

    def decide_human_movement() -> List[str]:
        move_human_dict = decide_human_move()
        move_human(move_human_dict)
        post_human_list = listup_obst_post_human(list(move_human_dict.keys()))
        post_human_dict = decide_obst_post(post_human_list)
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
