text = [line.strip() for line in open('inputtxt/day12input.txt')]

x = 0
y = 0
turn = 1
DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]

for line in text:
    cmd = line[0]
    number = int(line[1:])
    if cmd == 'R':
        for _ in range(number // 90):
            turn = (turn + 1) % 4
    elif cmd == 'L':
        for _ in range(number // 90):
            turn = (turn + 3) % 4
    elif cmd == 'N':
        y += number
    elif cmd == 'S':
        y -= number
    elif cmd == 'E':
        x += number
    elif cmd == 'W':
        x -= number
    elif cmd == 'F':
        x += DX[turn] * number
        y += DY[turn] * number

print(abs(x) + abs(y))


x1 = 10
y1 = 1
x = 0
y = 0
for line in text:
    cmd = line[0]
    number = int(line[1:])
    if cmd == 'N':
        y1 += number
    elif cmd == 'S':
        y1 -= number
    elif cmd == 'E':
        x1 += number
    elif cmd == 'W':
        x1 -= number
    elif cmd == 'L':
        for _ in range(number // 90):
            x1, y1, = -y1, x1
    elif cmd == 'R':
        for _ in range(number // 90):
            x1, y1 = y1, -x1
    elif cmd == 'F':
        x += number * x1
        y += number * y1
print(abs(x) + abs(y))