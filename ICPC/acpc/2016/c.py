n = int(input())
a = [int(i) for i in input().split()]
zero = sum(map(lambda  x: x%3 == 0, a))
one = sum(map(lambda  x: x%3 == 1, a))
two = sum(map(lambda  x: x%3 == 2, a))
onetwo = min(one, two)
one -= onetwo * 2
two -= onetwo * 2
