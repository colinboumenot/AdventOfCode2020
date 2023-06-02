text = open('inputtxt/day20input.txt').read().splitlines()
from collections import defaultdict
from copy import deepcopy
import math
text.append('')
grid = {}
tile = None
current = []

for line in text:
    line = line.strip()
    if 'Tile' in line:
        name = int(line.split()[1][:-1])
    elif line:
        current.append(list(line))
    else:
        grid[name] = current
        current = []

edges = {}
for key, value in grid.items():
    left, right, up, down = [], [], [], []
    for x in range(10):
        left.append(value[x][0])
        right.append(value[x][9])
    for y in range(10):
        up.append(value[0][y])
        down.append(value[9][y])
    edge = [tuple(x) for x in [left, right, up, down]]
    edges[key] = set([x for x in edge] + [tuple(reversed(x)) for x in edge])


edge_dict = defaultdict(set)
start = None
answer = 1
for key, item in edges.items():
    for key_2, item_2 in edges.items():
        if key != key_2:
            if item & item_2:
                edge_dict[key].add(key_2)
    if len(edge_dict[key]) == 2:
        start = key
        answer *= key
print(answer)

def rotate(tile):
    row = len(tile)
    col = len(tile[0])
    return_tile = [['?' for _ in range(row)] for _ in range(col)]
    for x in range(row):
        for y in range(col):
            return_tile[y][row-1-x] = tile[x][y]
    return return_tile
def match(x, y, dx, dy):
    if dx == -1:
        for z in range(10):
            if x[0][z] != y[9][z]:
                return False
        return True
    elif dy == 1:
        for z in range(10):
            if x[z][9] != y[z][0]:
                return False
        return True
    elif dx == 1:
        for z in range(10):
            if x[9][z] != y[0][z]:
                return False
        return True
    elif dy == -1:
        for z in range(10):
            if x[z][0] != y[z][9]:
                return False
        return True

def new_list(l):
    return_list = set()
    flipped = [deepcopy(l), list(reversed(l))]
    for _ in range(4):
        for x in range(len(flipped)):
            return_list.add(tuple([tuple(y) for y in flipped[x]]))
            flipped[x] = rotate(flipped[x])
    return return_list

placed = [[None for _ in range(int(math.sqrt(len(edges))))] for _ in range(int(math.sqrt(len(edges))))]
used = set()
placed[0][0] = start
placed[0][1], placed[1][0] = edge_dict[start]
used.add(placed[0][0])
used.add(placed[0][1])
used.add(placed[1][1])
while True:
    if len(used) == int(math.sqrt(len(edges))) * int(math.sqrt(len(edges))):
        break
    for x in range(int(math.sqrt(len(edges)))):
        for y in range(int(math.sqrt(len(edges)))):
            if placed[x][y] is not None:
                continue
            moves = set([z for z in edge_dict.keys() if z not in used])
            for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                xx, yy = x + dx, y + dy
                if 0 <= xx < int(math.sqrt(len(edges))) and 0 <= yy < int(math.sqrt(len(edges))) and placed[xx][yy]:
                    moves = moves & edge_dict[placed[xx][yy]]
            if len(moves) == 1:
                move = list(moves)[0]
                placed[x][y] = move
                used.add(move)
spaces = [[None for _ in range(int(math.sqrt(len(edges))))] for _ in range(int(math.sqrt(len(edges))))]
for x in range(int(math.sqrt(len(edges)))):
    for y in range(int(math.sqrt(len(edges)))):
        moves = new_list(grid[placed[x][y]])
        for dx, dy in [(0,1), (1,0), (-1,0), (0, -1)]:
            xx, yy = x + dx, y + dy
            if 0 <= xx < int(math.sqrt(len(edges))) and 0 <= yy < int(math.sqrt(len(edges))):
                valid = set()
                moves_x = new_list(grid[placed[xx][yy]])
                for xz in moves:
                    for yz in moves_x:
                        if match(xz, yz, dx, dy):
                            valid.add(xz)
                moves = moves & valid
        spaces[x][y] = list(moves)[0]

image = [['?' for _ in range(int(math.sqrt(len(edges))) * 8)] for _ in range(int(math.sqrt(len(edges))) * 8)]
for x in range(int(math.sqrt(len(edges)))):
    for y in range(int(math.sqrt(len(edges)))):
        temp = spaces[x][y]
        for dx in range(1, len(temp) - 1):
            for dy in range(1, len(temp[dx]) - 1):
                image[x * 8 + (dx - 1)][y * 8 + (dy - 1)] = temp[dx][dy]
monster = ['                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   ']

for i in new_list(image):
    current = [[False for _ in range(len(i[0]))] for _ in range(len(i))]
    contains = False
    for x in range(len(image)):
        for y in range(len(image[0])):
            is_monster = True
            for dx in range(len(monster)):
                for dy in range(len(monster[0])):
                    if not (0 <= x + dx < len(image) and 0 <= y + dy < len(image[0])):
                        is_monster = False
                    else:
                        if monster[dx][dy] == '#' and i[x+dx][y+dy] != '#':
                            is_monster = False
            if is_monster:
                contains = True
                for dx in range(len(monster)):
                    for dy in range(len(monster[0])):
                        if monster[dx][dy] == '#':
                            current[x+dx][y+dy] = True
    if contains:
        answer = 0
        for x in range(len(image)):
            for y in range(len(image[0])):
                if i[x][y] == '#' and not current[x][y]:
                    answer += 1
        print(answer)
