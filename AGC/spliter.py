from collections import defaultdict
import glob
import os
import re
INIT = """
#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#solve
"""


def exstract_each_solver_from_one_file():
    for i in range(200):
        try:
            with open(str(i)+".py", "r", encoding="utf-8") as f:
                d = defaultdict(list)
                ch = "N"
                for line in f:
                    if "# A" in line:
                        ch = "A"
                        d[ch].append(INIT)
                    elif "# B" in line:
                        ch = "B"
                        d[ch].append(INIT)
                    elif "# C" in line:
                        ch = "C"
                        d[ch].append(INIT)
                    elif "# D" in line:
                        ch = "D"
                        d[ch].append(INIT)
                    elif "# E" in line:
                        ch = "E"
                        d[ch].append(INIT)
                    elif "# F" in line:
                        ch = "F"
                        d[ch].append(INIT)
                    elif "#Solve" in line:
                        ch = "N"
                    elif "#G" in line:
                        ch = "N"
                    else:
                        if ch != "N":
                            d[ch].append(line)
                os.makedirs(str(i), exist_ok=True)
                for k, v in d.items():
                    with open(str(i)+"/"+k.lower()+".py", "w", encoding="utf-8") as o:
                        # print("".join(v))
                        c = "".join(v)
                        c = re.sub(r"#solve\n+\"\"\"\n(([^\n]*\n)*)\"\"\"", "#solve\n\\1", c)
                        c = re.sub(r"# A\n+\"\"\"\n(([^\n]*\n)*)\"\"\"", "# A\n\\1", c)
                        c = re.sub(r"# B\n+\"\"\"\n(([^\n]*\n)*)\"\"\"", "# B\n\\1", c)
                        c = re.sub(r"# C\n+\"\"\"\n(([^\n]*\n)*)\"\"\"", "# C\n\\1", c)
                        c = re.sub(r"# D\n+\"\"\"\n(([^\n]*\n)*)\"\"\"", "# D\n\\1", c)
                        c = re.sub(r"# E\n+\"\"\"\n(([^\n]*\n)*)\"\"\"", "# E\n\\1", c)
                        c = re.sub(r"# F\n+\"\"\"\n(([^\n]*\n)*)\"\"\"", "# F\n\\1", c)
                        o.write(c)

        except Exception as e:
            print(e)
            pass

for i in range(1,100):
    try:
        os.rename("./" + str(i), f"./{i:03}")
    except Exception as e:
        print(e)
        pass