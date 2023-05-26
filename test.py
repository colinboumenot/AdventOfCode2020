import itertools
from collections import defaultdict


def clean_up(text, dimensions):
    set_up = (0,) * (dimensions - 2)
    return {(x, y) + set_up for y, r in enumerate(text) for x, col in enumerate(r) if col == '#'}


def get_neighbors(location):
    dimensions = len(location)
    neighbors = set()
    for change in itertools.product([-1, 0, 1], repeat=dimensions):
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


def answer_finder(lights_on):
    for _ in range(6):
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

initial_state_3d = clean_up(text, 3)
print("Part 1:", answer_finder(initial_state_3d))

initial_state_4d = clean_up(text, 4)
print("Part 2:", answer_finder(initial_state_4d))
