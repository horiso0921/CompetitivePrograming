import sys
import collections
sys.setrecursionlimit(10**5)

def basic(pre_field, goal_field):
    """
    基本実装
    初期盤面が目標盤面に到達するかを計測し目標盤面に至るまでの手数と手筋を返す
    目標盤面に到達できない場合は空のlistを返す

    param
    ------
    pre_field: list[int]
    goal_filed: list[int]

    return
    ------
    troubles: list[int]
    len_troubles: int
    """
    troubles = collections.deque()
    check = collections.defaultdict(int)

    diff = float("inf")
    field_range = len(pre_field)
    def dfs(current_field, goal_field):
        current_field_number_coordinate_dict = collections.defaultdict(tuple)
        for height in range(field_range):
            for column in range(field_range):
                current_field_number_coordinate_dict[current_field[height][column]] = (height, column)
        tmp = []
        for number in range(1, field_range ** 2 + 1):
            number_current_coordinate = current_field_number_coordinate_dict[number]
            tmp.append(number_current_coordinate[0] + number_current_coordinate[1] * field_range)
        if check[tuple(tmp)]: return False
        print(current_field)
        check[tuple(tmp)] = 1
        for ope in (1,-1):
            for column in range(field_range):
                tmp_field = [[current_field[tmp_heigh][tmp_col] if tmp_col != column 
                                else current_field[(tmp_heigh + ope)%field_range][tmp_col] for tmp_col in range(field_range)] for tmp_heigh in range(field_range)]
                if calc_diff(tmp_field, goal_field) == 0:
                    tmp_ope = 1 if ope == -1 else 2
                    operate = [2, column + 1, tmp_ope]
                    troubles.appendleft(operate)
                    return True
                if dfs(tmp_field, goal_field):
                    tmp_ope = 1 if ope == -1 else 2
                    operate = [2, column + 1, tmp_ope]
                    troubles.appendleft(operate)
                    return True
            for height in range(field_range):
                tmp_field = [[current_field[tmp_heigh][tmp_col] if tmp_heigh != height
                                else current_field[tmp_heigh][(tmp_col + ope)%field_range] for tmp_col in range(field_range)] for tmp_heigh in range(field_range)]
                if calc_diff(tmp_field, goal_field) == 0:
                    tmp_ope = 1 if ope == -1 else 2
                    operate = [1, height + 1, tmp_ope]
                    troubles.appendleft(operate)
                    return True
                if dfs(tmp_field, goal_field):
                    tmp_ope = 1 if ope == -1 else 2
                    operate = [1, height + 1, tmp_ope]
                    troubles.appendleft(operate)
                    return True
        return False
    if dfs(pre_field, goal_field):
        return troubles, len(troubles)
    else:
        return [], 0

def calc_diff(current_field, goal_field):
    current_field_number_coordinate_dict = collections.defaultdict(tuple)
    goal_field_number_coordinate_dict = collections.defaultdict(tuple)
    field_range = len(current_field)

    for height in range(field_range):
        for column in range(field_range):
            current_field_number_coordinate_dict[current_field[height][column]] = (height, column)
            goal_field_number_coordinate_dict[goal_field[height][column]] = (height, column)
    
    diff = 0

    for number in range(1, field_range ** 2 + 1):
        number_current_coordinate = current_field_number_coordinate_dict[number]
        number_goal_coordinate = goal_field_number_coordinate_dict[number]
        column_diff = min((number_current_coordinate[0] - number_goal_coordinate[0]) % field_range,
                        -(number_current_coordinate[0] - number_goal_coordinate[0]) % field_range) 
        height_diff = min((number_current_coordinate[1] - number_goal_coordinate[1]) % field_range,
                        -(number_current_coordinate[1] - number_goal_coordinate[1]) % field_range)
        diff += column_diff + height_diff
    return diff

def main(lines):
    number_of_line = int(lines[0])
    pre_field = [[int(i) for i in line.split()] for line in lines[1:number_of_line + 1]]
    goal_field = [[int(i) for i in line.split()] for line in lines[number_of_line + 1:]]
    print(pre_field)
    if number_of_line == 2 or number_of_line == 3:
        troubles, len_troubles = basic(pre_field, goal_field)
        if len_troubles:
            print("yes")
            print(len_troubles)
            for trouble in troubles:
                print(*trouble)
        else:
            print("no")
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
