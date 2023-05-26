text = open('inputtxt/day17input.txt').read().strip().splitlines()
import itertools
from collections import Counter

def clean_up(text, dimensions):
    set_up = (0,) * (dimensions - 2)
    return {(x,y) + set_up for y, r in enumerate(text) for x, col in enumerate(r) if col == '#'}

def move(lights_on):
    adjacent = (tuple(map(sum, zip(location, change))) for location in
                lights_on for change in itertools.product([-1, 0, 1], repeat = len(location)) if any(change))
    return {location for location, value in Counter(adjacent).items() if value == 3 or (location in lights_on and value == 2)}

def answer_finder(lights_on):
    for x in range(6):
        lights_on = move(lights_on)
    return len(lights_on)

print(answer_finder(clean_up(text, 3)))
print(answer_finder(clean_up(text, 4)))
