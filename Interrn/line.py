import sys
from collections import defaultdict, deque

field_memo = defaultdict(int)

def solve_optimal_placement(one_side_length, fields):
    """
    最適な○の置き方を解く

    Parameters
    ----------
    fields : list[str]
        盤面(○×.の状態)
    one_side_length : int
        盤面の幅

    Returns
    -------
    optimal_placement : list[list[str]]
    """

    cross_list = []

    for vertical in range(one_side_length):
        for side in range(one_side_length):
            if fields[vertical][side] == "×":
                cross_list.append((vertical, side))

    dot_list = []
    for vertical in range(one_side_length):
        for side in range(one_side_length):
            if fields[vertical][side] == ".":
                dot_list.append((vertical, side))
    
    optimal_placement = dot_list

    return dot_list
    # dfs(one_side_length, cross_list, [])

def dfs(one_side_length, cross_list, circle_list):
    tmp_cross_list = cross_list[::1]
    for cross_vertical, cross_side in cross_list:
        for move_vertical, move_side in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            cross_vertical_next = move_vertical + cross_vertical
            cross_side_next = move_side + cross_side
            
            if 0 <= cross_side_next < one_side_length and 0 <= cross_vertical < one_side_length:
                if not (cross_vertical_next, cross_vertical_next) in circle_list:
                    dfs(one_side_length, tmp_cross_list, circle_list + [(cross_vertical_next, cross_vertical_next)])
                    tmp_cross_list.append((cross_vertical, cross_side))


def check(cross_list, circle_list, new_circle):
    for old_circle in circle_list:
        if new_circle[0] == old_circle[0]:
            vertical = new_circle[0]
            for side in range(min(new_circle[1], old_circle[1]) + 1, min(new_circle[1], old_circle[1])):
                if not (vertical, side) in cross_list:
                    break
            else:
                for side in range(min(new_circle[1], old_circle[1]) + 1, min(new_circle[1], old_circle[1])):
                    cross_list.remove((vertical, side))
        elif new_circle[1] == old_circle[1]:
            side = new_circle[1]
            for vertical in range(min(new_circle[0], old_circle[0]) + 1, min(new_circle[0], old_circle[0])):
                if not (vertical, side) in cross_list:
                    break
            else:
                for side in range(min(new_circle[0], old_circle[0]) + 1, min(new_circle[0], old_circle[0])):
                    cross_list.remove((vertical, side))
        elif new_circle[1] - new_circle[0] == old_circle[1] - old_circle[0]:
            for i in range(abs(new_circle[0] - old_circle[1])):
                if new_circle[0] > old_circle[0]:
                    f0 = -1
                else:
                    f0 = 1
                if new_circle[1] > old_circle[1]:
                    f1 = -1
                else:
                    f1 = 1


def main(lines):

    n = int(lines[0])

    fields = lines[1:]

    answer = solve_optimal_placement(n,fields)

    print(len(answer))
    
    for i in range(len(answer)):
        print(*answer[i])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
