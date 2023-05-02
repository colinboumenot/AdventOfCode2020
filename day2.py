text = open('inputtxt/day2input.txt').read().splitlines()

count = 0

for line in text:
    valid, line = line.split(':')
    range, letter = valid.split(' ')
    minimum, maximum = range.split('-')
    letters = 0
    for letter_x in [x for x in line]:
        if letter_x == letter:
            letters += 1
    if int(minimum) <= letters <= int(maximum):
        count += 1
print(count)

count = 0
for line in text:
    valid, line = line.split(':')
    range, letter = valid.split(' ')
    minimum, maximum = range.split('-')
    characters = [x for x in line]
    if characters[int(minimum)] == letter:
        if characters[int(maximum)] != letter:
            count += 1
    elif characters[int(maximum)] == letter:
        if characters[int(minimum)] != letter:
            count += 1
print(count)