import sys
from heapq import heappush, heappop
from collections import defaultdict
from typing import List, Tuple
INF = float("INF")

class Field:
    
    MOVE_DIRECTION:List[Tuple[int, int]] = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    OBSTACLE:str = "#"
    
    def __init__(self, row:int, column:int, field:List[str]) -> None:
        self.row:int = row
        self.column:int = column
        self.field:List[str] = field
        self.obstacle_num: int = self.count_obstacle()
    
    def count_obstacle(self) -> int:
        """フィールド内に存在する壁の数を返す

        Returns:
            int: 壁の数
        """
        obst_num = 0
        for line in self.field:
            obst_num += line.count(self.OBSTACLE)
        return obst_num

    def search_specific_box(self, specific_box:str) -> Tuple[int, int]:
        """特定の点の座標を探す

        Args:
            specific_box (str): 特定の点を表す文字列

        Returns:
            Tuple[int, int]: 座標（行，列）
        """
        for row in range(self.row):
            for column in range(self.column):
                if self.field[row][column] == specific_box:
                    return (row, column)
        return (-1, -1)
    
    def is_there_obstacle(self, now_row:int, now_column:int) -> bool:
        """特定の点が障害物なのか返す

        Args:
            now_row (int): 特定の点の行
            now_column (int): 特定の点の列

        Returns:
            bool: 特定の点が障害物なのか
        """
        return self.field[now_row][now_column] == "#"

    def is_inside_field(self, now_row:int, now_column:int) -> bool:
        """特定の点がフィールドの内部なのか返す

        Args:
            now_row (int): 特定の点の行
            now_column (int): 特定の点の列

        Returns:
            bool: 特定の点がフィールドの内部なのか
        """
        return 0 <= now_row < self.row and 0 <= now_column < self.column
    
    def dijkstra(self, start_row:int, start_column:int, goal_row:int, goal_column:int) -> int:
        """スタートからゴールまでにかかる時間を拡張ダイクストラで計測する
            拡張時にはこれまで破壊した障害物の数入れる
            また，障害物はフィールドに存在する物以上破壊されることがないので
                一定以上の障害物を破壊するという挙動になった場合枝狩りをする
            
            TODO
            このコードだと二度同じ障害物を破壊するという行為が発生しているため，
                無駄な計算をしている．
                特に一番無駄なのは前回破壊した壁をもう一回破壊する行動．
                これを削ればもう少しパフォ―マスが良くなる

        Args:
            start_row (int): スタートの行
            start_column (int): スタートの列
            goal_row (int): ゴールの行
            goal_column (int): ゴールの列

        Returns:
            int: ゴールまでにかかる時間
        """
        dist = defaultdict(lambda: INF)
        dist[(start_row, start_column, 0)] = 0
        q = [(0, start_row, start_column, 0)]
        while q:
            spend_time, now_row, now_column, broken_obst = heappop(q)
            
            if now_row == goal_row and now_column == goal_column:
                return spend_time
            
            if dist[(now_row, now_column, broken_obst)] < spend_time:
                continue 
            
            for dia_row, dia_column in self.MOVE_DIRECTION:
                next_row = dia_row + now_row
                next_column = dia_column + now_column
                if self.is_inside_field(next_row, next_column):
                    next_time = spend_time + 1
                    next_broken_obst = broken_obst
                    if self.is_there_obstacle(next_row, next_column):
                        next_time += broken_obst
                        next_broken_obst += + 1
            
                    # 枝狩り
                    if next_broken_obst > self.obstacle_num:
                        continue
            
                    if dist[(next_row, next_column, next_broken_obst)] > next_time:
                        dist[(next_row, next_column, next_broken_obst)] = next_time
                        heappush(q, (next_time, next_row, next_column, next_broken_obst))

    def calculation_time_from_A_to_B(self, start_row:int, start_column:int, goal_row:int, goal_column:int) -> int:
        """ある点からある点までにかかる時間を計測する

        Args:
            start_row (int): スタートの行
            start_column (int): スタートの列
            goal_row (int): ゴールの行
            goal_column (int): ゴールの列

        Returns:
            int: ゴールまでにかかる時間
        """
        return self.dijkstra(start_row, start_column, goal_row, goal_column)
    
def solve(row:int, column:int, field: List[str]):
    
    gorilla_field = Field(row, column, field)
    start_row, start_column = gorilla_field.search_specific_box("S")
    goal_row, goal_column = gorilla_field.search_specific_box("G")
    
    ans_time = gorilla_field.calculation_time_from_A_to_B(start_row, start_column, goal_row, goal_column)
    print(ans_time)
    


def main():
    N,M = map(int, sys.stdin.readline().split())
    S = [sys.stdin.readline() for _ in range(N)]
    solve(N,M,S)

if __name__ == "__main__":
    main()