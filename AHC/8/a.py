from collections import defaultdict, deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
from typing import Dict, List, Tuple

import sys
import itertools
import math

from attr import field
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
PET = 2
HUMAN = 3
VACANT = 1
num_to_UDLR = ["U", "D", "L", "R"]
UDLR_to_movement = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
num_to_udlr = ["u", "d", "l", "r"]
udlr_to_movement = {"u": (0, -1), "d": (0, 1), "l": (-1, 0), "r": (1, 0)}


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

    def can_post_obst(y: int, x: int):
        return field[y][x] % PET != 0

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

    def move_human(s: List[str]):
        for i in range(m):
            x, y = h[i]
            y, x = move_obj(s[i], y, x, HUMAN)
            h[i] = [x, y]
        return

    def decide_human_move() -> List[str]:
        return ["."] * m

    for i in range(300):
        movement = decide_human_move()
        print("".join(movement), flush=True)
        move_pet(LS())
    return


# main
if __name__ == '__main__':
    solve()
