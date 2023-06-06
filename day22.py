text = open('inputtxt/day22input.txt').read().splitlines()
from collections import deque

player_one = deque()
player_two = deque()
current = player_one

for line in text:
    if 'Player' in line and '2' in line:
        current = player_two
    elif line and 'Player' not in line:
        current.append(int(line))

while len(player_one) > 0 and len(player_two) > 0:
    move_one = player_one.popleft()
    move_two = player_two.popleft()
    if move_one > move_two:
        player_one.extend([move_one, move_two])
    else:
        player_two.extend([move_two, move_one])
player_one = list(player_one)
print(sum((index + 1) * value for index, value in enumerate(player_one[::-1])))