def main():
    s = input()
    ans = list(input())
    s = reversed(s)
    for si in s:
        if si == "C":
            ans = ans[1:] + [ans[0]]
        if si == "J":
            ans = [ans[-1]] + ans[:-1]
        if si == "E":
            tmp = [ans[len(ans) // 2]] if len(ans) & 1 else []
            ans = ans[len(ans) // 2 + (len(ans) & 1):] + tmp + ans[: len(ans) // 2]
        if si == "A":
            ans = ans[::-1]
        if si == "M":
            for i in range(len(ans)):
                if ans[i].isdecimal():
                    ans[i] = int(ans[i])
                    ans[i] = str((ans[i] + 1) % 10)
        if si == "P":
            for i in range(len(ans)):
                if ans[i].isdecimal():
                    ans[i] = int(ans[i])
                    ans[i] = str((ans[i] - 1) % 10)

    print("".join(ans))



if __name__ == "__main__":
    for _ in range(int(input())):
        main()