text = str(open('inputtxt/day23input.txt').read())
text = [int(x) for x in text]
neighbor = [None for _ in range(11)]

from copy import deepcopy
moveable_text = deepcopy(text)
moveable_neighbor = deepcopy(neighbor)

for x in range(len(moveable_text)):
    moveable_neighbor[moveable_text[x]] = moveable_text[(x+1) % len(moveable_text)]
count = 0
current = moveable_text[0]
for _ in range(100):
    count += 1
    selected = moveable_neighbor[current]
    moveable_neighbor[current] = moveable_neighbor[moveable_neighbor[moveable_neighbor[selected]]]



