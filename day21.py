text = open('inputtxt/day21input.txt').read().splitlines()
from copy import deepcopy
allergens = {}
ingredients = []

for line in text:
    ingredient, known = line.strip(')').split(' (contains ')
    ingredients += ingredient.split()
    for allergen in known.split(', '):
        if allergen not in allergens:
            allergens[allergen] = set(ingredient.split())
        else:
            allergens[allergen] &= set(ingredient.split())

allergen_to_code = {}
total = 0
while total <= 8:
    for key, value in allergens.items():
        if len(value) == 1:
            total += 1
            allergen_to_code[key] = value
            for key_2, value_2 in allergens.items():
                if key != key_2:
                    allergens[key_2] -= value

for key, value in allergens.items():
    if key not in allergen_to_code:
        allergen_to_code[key] = value
allergen_copy = deepcopy(allergen_to_code)
codes = list(value.pop() for value in allergen_copy.values())
print(sum(x not in codes for x in ingredients))
print(allergen_to_code)
answer = codes[3] + ',' + codes[1] + ',' + codes[6] + ',' + codes[4] + ',' + codes[0] + ',' + codes[2] + ',' + codes[5] + ',' + codes[7]
print(answer)

