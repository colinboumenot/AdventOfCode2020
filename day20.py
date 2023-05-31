text = open('inputtxt/day20input.txt').read().splitlines()
from collections import defaultdict
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

