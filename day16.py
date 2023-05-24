text = open('inputtxt/day16input.txt').read().strip().splitlines()
import re

limits = []
available = None
leftover = []
for line in text:
    values = [int(x) for x in re.findall('\d+', line)]
    if len(values) == 4:
        limits.append(values)
    elif len(values) > 4:
        if available is None:
            available = values
        else:
            leftover.append(values)
answer = 0
VALID = [[True for _ in range(len(limits))] for _ in range(len(limits))]

for values in leftover:
    valid_x = True
    for value in values:
        valid = False
        for a, b, c, d in limits:
            if a <= value <= b or c <= value <= d:
                valid = True
        if not valid:
            answer += value
            valid_x = False
    if valid_x:
        for k, v in enumerate(values):
            for j, (a, b, c, d) in enumerate(limits):
                if not (a <= v <= b or c <= v <= d):
                    VALID[k][j] = False
print(answer)

MAP = [None for _ in range(20)]
USED = [False for _ in range(20)]
located = 0
while True:
    for x in range(20):
        line = [z for z in range(20) if VALID[x][z] and not USED[z]]
        if len(line) == 1:
            MAP[x] = line[0]
            USED[line[0]] = True
            located += 1
    if located == 20:
        break
answer = 1
for key, value in enumerate(MAP):
    if value < 6:
        answer *= available[key]
print(answer)
