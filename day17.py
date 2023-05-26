#text = open('inputtxt/day17input.txt').read().strip().splitlines()
import itertools
from collections import Counter, defaultdict
import time

def clean_up(text, dimensions):
    set_up = (0,) * (dimensions - 2)
    return {(x,y) + set_up for y, r in enumerate(text) for x, col in enumerate(r) if col == '#'}

def get_neighbors(location):
    dimensions = len(location)
    neighbors = set()
    for change in itertools.product([-1, 0, 1], repeat = dimensions):
        neighbor = tuple(map(sum, zip(location, change)))
        if neighbor != location:
            neighbors.add(neighbor)
    return neighbors
def move(lights_on):
    neighbors = defaultdict(int)
    for location in lights_on:
        for neighbor in get_neighbors(location):
            neighbors[neighbor] += 1
    new_lights = set()
    for location, count in neighbors.items():
        if count == 3 or (location in lights_on and count == 2):
            new_lights.add(location)
    return new_lights
    #return {location for location, value in Counter(adjacent).items() if value == 3 or (location in lights_on and value == 2)}

def answer_finder(lights_on):
    for x in range(6):
        lights_on = move(lights_on)
    return len(lights_on)


text = [
    "....#...",
    ".#..###.",
    ".#.#.###",
    ".#....#.",
    "...#.#.#",
    "#.......",
    "##....#.",
    ".##..#.#"
]

start = time.time()
print(answer_finder(clean_up(text, 3)))
print(answer_finder(clean_up(text, 4)))
print(time.time() - start)
