text = open('inputtxt/day14input.txt').read().splitlines()

def index_getter(id, floating):
    if len(floating) == 0:
        return [id]
    else:
        base = floating[0]
        remainder = floating[1:]
        answer = index_getter(id, remainder) + index_getter(id + 2 ** base, remainder)
        return answer

def modify(value, mask):
    return_value = 0
    for index, bit in enumerate(reversed(mask)):
        if bit == 'X':
            return_value += (value & (2 ** index))
        elif bit == '1':
            return_value += 2 ** index
    return return_value

def modify_two(id, mask):
    return_index = 0
    floating = []
    for index, bit in enumerate(reversed(mask)):
        bit_x = id & (2 ** index)
        if bit == 'X':
            floating.append(index)
        elif bit == '1':
            return_index += 2 ** index
        elif bit == '0':
            return_index += bit_x
            pass
    return index_getter(return_index, floating)



mask = ''
memory = {}

for line in text:
    if line.startswith('mask'):
        new_mask = line.split()[-1]
        mask = new_mask
    else:
        id, _, value = line.split()
        id = int(id.split('[')[-1][:-1])
        value = int(value)
        I = [id]
        value = modify(value, mask)

        for x in I:
            memory[x] = value
answer = 0
for x, y in memory.items():
    answer += y
print(answer)

mask = ''
memory = {}

for line in text:
    if line.startswith('mask'):
        new_mask = line.split()[-1]
        mask = new_mask
    else:
        id, _, value = line.split()
        id = int(id.split('[')[-1][:-1])
        value = int(value)
        I = modify_two(id, mask)

        for x in I:
            memory[x] = value

answer = 0
for x, y in memory.items():
    answer += y
print(answer)


