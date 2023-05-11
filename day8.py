text = open('inputtxt/day8input.txt').read().splitlines()


visited = set()
accumulator = 0
index = 0

while index < len(text):
    line = text[index]
    if index in visited:
        print(accumulator)
        break
    else:
        visited.add(index)

    command, value = line.split(' ')
    if command == 'acc':
        accumulator += int(value)
        index += 1
    if command == 'jmp':
        index += int(value)
    if command == 'nop':
        index += 1


def search(text_x):
    visited = set()
    index = 0
    accumulator = 0

    while index < len(text_x):
        line = text_x[index]
        if index in visited:
            return False
        else:
            visited.add(index)

        command, value = line.split(' ')
        if command == 'acc':
            accumulator += int(value)
            index += 1
        if command == 'jmp':
            index += int(value)
        if command == 'nop':
            index += 1

    return accumulator

for x in range(len(text)):
    fake = open('inputtxt/day8input.txt').read().splitlines()
    if text[x].split(' ')[0] == 'nop':
        fake[x] = 'jmp' + ' ' + str(text[x].split(' ')[1])
        if search(fake) is not False:
            print(search(fake))
            break
        else:
            fake[x] = text[x]

for x in range(len(text)):
    fake = open('inputtxt/day8input.txt').read().splitlines()
    if text[x].split(' ')[0] == 'jmp':
        fake[x] = 'nop' + ' ' + str(text[x].split(' ')[1])
        if search(fake) is not False:
            print(search(fake))
            break
        else:
            fake[x] = text[x]



