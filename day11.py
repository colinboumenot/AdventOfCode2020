text = [list(line.strip()) for line in list(open('inputtxt/day11input.txt').read().splitlines())]
print(text)
from copy import deepcopy

length = len(text)
width = len(text[0])

def evolve(text_x, part_one = True):
    while True:
        copy = deepcopy(text_x)
        change = False
        for x in range(length):
            for y in range(width):
                z = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if not (dx == 0 and dy == 0):
                            nx = dx + x
                            ny = dy + y
                            while 0 <= nx < length and 0 <= ny < width and text_x[nx][ny] == '.' and (not part_one):
                                nx += dx
                                ny += dy
                            if 0 <= nx < length and 0 <= ny < width and text_x[nx][ny] == '#':
                                z += 1
                if text_x[x][y] == 'L':
                    if z == 0:
                        copy[x][y] = '#'
                        change = True
                elif text_x[x][y] == '#' and z >= (4 if part_one else 5):
                    copy[x][y] = 'L'
                    change = True
        if not change:
            break
        text_x = deepcopy(copy)
    answer = 0
    for x in range(length):
        for y in range(width):
            if text_x[x][y] == '#':
                answer += 1
    return answer

print(evolve(text, True))
print(evolve(text, False))
