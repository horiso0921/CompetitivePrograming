sum = 0
for i in range(100):
    with open(f"score\{i:04}.txt", "r") as t:
        for line in t:
            line = line.lstrip("Score = ").rstrip()
            try:
                sum += int(line)
            except:
                pass
print(sum)
            