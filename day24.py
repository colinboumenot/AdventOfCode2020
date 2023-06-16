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