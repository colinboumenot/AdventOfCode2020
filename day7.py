text = open('inputtxt/day7input.txt').read().splitlines()
from collections import defaultdict
import re

neighbors = defaultdict(set)

def contains_gold(node):
    if node == 'shiny gold':
        return True
    else:
        return any(contains_gold(neighbor) for _, neighbor in neighbors[node])

for line in text:
    parent = ' '.join(line.split()[:2])
    neighbors[parent] = (re.findall(r'(\d+?) (.+?) bags?', str(line)))

count = 0

for node in neighbors:
    if contains_gold(node):
        count += 1

print(count - 1)

def count(node):
    return 1 + sum(int(bags) * count(node_x) for bags, node_x in neighbors[node])

print(count('shiny gold') - 1)




