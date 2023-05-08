text = open('inputtxt/day6input.txt').read().split('\n\n')

count = 0

for line in text:
    total = set()
    for character in line:
        if character in 'abcdefghijklmnopqrstuvwxyz':
            total.add(character)
    count += len(total)

print(count)

count = 0
for line in text:
    lines = line.split('\n')
    first = set(lines[0])
    for x in lines:
        first = set(x) & first
    count += len(first)

print(count)

