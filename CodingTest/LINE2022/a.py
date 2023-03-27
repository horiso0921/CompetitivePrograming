import sys
import bisect
from typing import List, Tuple

def has_all_range_number(number_lis:List[int], left_val:int, right_val:int) -> bool:
    """半開区間で受け取る範囲の数字がすべてlistに含まれるかを返す
    [l, r)

    Args:
        number_lis (List[int]): 数字のリスト
        left_val (int): 左端の数字
        right_val (int): 右端の数字

    Returns:
        bool: 半開区間で受け取る範囲の数字がすべてlistに含まれるか
    """
    min_val_index_than_right = bisect.bisect_left(number_lis, right_val)
    min_val_index_than_left = bisect.bisect_left(number_lis, left_val)
    return right_val - left_val == min_val_index_than_right - min_val_index_than_left

def search_min_number_no_contain_in_range(number_lis:List[int], left_val:int, right_val:int) -> int:
    """範囲内にある数字の中でlistに含まれておらず一番小さい値を返す

    Args:
        number_lis (List[int]): 数字のリスト
        left_val (int): 左端の数字
        right_val (int): 右端の数字

    Returns:
        int: 範囲内にある数字の中でlistに含まれておらず一番小さい値
    """
    ok = left_val - 1 # ここで1引かないと left_valが含まれることになる
    ng = right_val
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if has_all_range_number(number_lis, left_val, mid + 1):
            ok = mid
        else:
            ng = mid
    return ok + 1

def solve(A: List[int], LR:List[Tuple[int, int]]):
    for l, r in LR:
        if has_all_range_number(A, l, r+1):
            print(-1)
        else:
            min_number_no_contain_in_range = search_min_number_no_contain_in_range(A, l, r)
            print(min_number_no_contain_in_range)
            

def main():
    N,_ = map(int, sys.stdin.readline().split())
    A = [0] + [int(ai) for ai in sys.stdin.readline().split()] + [N + 1] 
    Q = int(sys.stdin.readline())
    LR = [(int(i) for i in sys.stdin.readline().split()) for _ in range(Q)]
    solve(A, LR)

if __name__ == "__main__":
    main()