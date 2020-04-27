import sys
from math import ceil

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
 
    weight, height, bmi = map(int, lines[0].split())
    ideal_weight = height ** 2 * bmi / 10 ** 4
    print(max(0, ceil(weight - ideal_weight)))

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)