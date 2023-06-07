text = open('inputtxt/day22input.txt').read().splitlines()
from collections import deque
from copy import deepcopy
player_one = deque()
player_two = deque()
current = player_one

for line in text:
    if 'Player' in line and '2' in line:
        current = player_two
    elif line and 'Player' not in line:
        current.append(int(line))
player_one_two = list(deepcopy(player_one))
player_two_two = list(deepcopy(player_two))

while len(player_one) > 0 and len(player_two) > 0:
    move_one = player_one.popleft()
    move_two = player_two.popleft()
    if move_one > move_two:
        player_one.extend([move_one, move_two])
    else:
        player_two.extend([move_two, move_one])
player_one = list(player_one)
print(sum((index + 1) * value for index, value in enumerate(player_one[::-1])))

def recursion(one, two):
    previous = set()
    while len(one) > 0 and len(two) > 0:
        if (tuple(one), tuple(two)) in previous:
            return True
        previous.add((tuple(one), tuple(two)))
        move_one = one.pop(0)
        move_two = two.pop(0)
        if len(one) >= move_one and len(two) >= move_two:
            winner = recursion(one[:move_one], two[:move_two])
            if winner:
                one.extend([move_one, move_two])
            else:
                two.extend([move_two, move_one])
        else:
            if move_one > move_two:
                one.extend([move_one, move_two])
            else:
                two.extend([move_two, move_one])
    return len(one) > 0

recursion(player_one_two, player_two_two)
print(sum((index + 1) * value for index, value in enumerate(player_one_two[::-1])))