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
    if current == 1:
        destination = 9
    else:
        destination = current - 1
    while destination in [selected, moveable_neighbor[selected], moveable_neighbor[moveable_neighbor[selected]]]:
        if destination == 1:
            destination = 9
        else:
            destination -= 1
    moveable_neighbor[moveable_neighbor[moveable_neighbor[selected]]] = moveable_neighbor[destination]
    moveable_neighbor[destination] = selected
    current = moveable_neighbor[current]
answer = []
x = moveable_neighbor[1]
while x != 1:
    answer.append(x)
    x = moveable_neighbor[x]
print(''.join([str(x) for x in answer]))

neighbor = [None for _ in range(1000001)]
moveable_text = deepcopy(text)
moveable_neighbor = deepcopy(neighbor)

for x in range(len(moveable_text)):
    moveable_neighbor[moveable_text[x]] = moveable_text[(x+1) % len(moveable_text)]
moveable_neighbor[moveable_text[-1]] = 10
for x in range(10, 1000001):
    moveable_neighbor[x] = x + 1
moveable_neighbor[-1] = moveable_text[0]

count = 0
current = moveable_text[0]
for _ in range(10000000):
    count += 1
    selected = moveable_neighbor[current]
    moveable_neighbor[current] = moveable_neighbor[moveable_neighbor[moveable_neighbor[selected]]]
    if current == 1:
        destination = 1000000
    else:
        destination = current - 1
    while destination in [selected, moveable_neighbor[selected], moveable_neighbor[moveable_neighbor[selected]]]:
        if destination == 1:
            destination = 1000000
        else:
            destination -= 1
    moveable_neighbor[moveable_neighbor[moveable_neighbor[selected]]] = moveable_neighbor[destination]
    moveable_neighbor[destination] = selected
    current = moveable_neighbor[current]
print(moveable_neighbor[1] * moveable_neighbor[moveable_neighbor[1]])
