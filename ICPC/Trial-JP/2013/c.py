from heapq import heappop, heappush

def main(n):
    rw = [[int(i) for i in input().split()] for _ in range(n)]
    rw.sort()
    s = sum(map(lambda x: x[0], rw))
    if s >= rw[-1][0] * 2:
        print(s + sum(map(lambda x: x[1], rw)))
    else:
        dp = [0] * 1001
        dp[0] = 1
        for r,w in rw[:-1]:
            for j in range(1000, -1, -1):
                if j + w <= 1000:
                    dp[j + w] |= dp[j]
        for j in range(rw[-1][0] - (s - rw[-1][0]), -1, -1):
            if dp[j]: break
        print(rw[-1][0] * 2 + sum(map(lambda x: x[1], rw)) - j)
        


while 1:
    n = int(input())
    if n == 0:
        break
    main(n)