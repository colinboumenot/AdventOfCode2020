text = open('inputtxt/day24input.txt').read().splitlines()

black_tiles = set()

for line in text:
    x, y, z = 0, 0, 0
    index = 0
    while line:
        if line.startswith('ne'):
            x += 1
            z -= 1
            line = line[2:]
        elif line.startswith('e'):
            x += 1
            y -= 1
            line = line[1:]
        elif line.startswith('se'):
            y -= 1
            z += 1
            line = line[2:]
        elif line.startswith('sw'):
            x -= 1
            z += 1
            line = line[2:]
        elif line.startswith('w'):
            x -= 1
            y += 1
            line = line[1:]
        else:
            z -= 1
            y += 1
            line = line[2:]
    if (x, y, z) in black_tiles:
        black_tiles.remove((x, y, z))
    else:
        black_tiles.add((x, y , z))
print(len(black_tiles))

moves = [(1, 0, -1), (-1, 0, 1), (1, -1, 0), (-1, 1, 0), (0, 1, -1), (0, -1, 1)]
for _ in range(100):
    final_black = set()
    checked = set()
    for (x, y, z) in black_tiles:
        checked.add((x, y, z))
        for (dx, dy, dz) in moves:
            checked.add((x + dx, y + dy, z + dz))
    for (x, y, z) in checked:
        answer = 0
        for (dx, dy, dz) in moves:
            if (x + dx, y + dy, z + dz) in black_tiles:
                answer += 1
        if (x, y, z) in black_tiles and (answer == 1 or answer == 2):
            final_black.add((x, y, z))
        if (x, y, z) not in black_tiles and answer == 2:
            final_black.add((x, y, z))
    black_tiles = final_black
print(len(black_tiles))
