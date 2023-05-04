import re
text = open('inputtxt/day4input.txt').read().strip().split('\n\n')
required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid = 0
valid_list = []
for line in text:
    fine = True
    for require in required:
        if not require in line:
            fine = False
    if fine:
        valid += 1
        valid_list.append(line)
print(valid)

text_two = open('inputtxt/day4input.txt').read().strip('\n')
data = [[x.split(':') for x in re.split(' |\n', y)] for y in text_two.split('\n\n')]

def check(data_x):
    fine = 0
    for entry in data_x:
        possible = False
        input, output = entry[0], entry[1]
        if input == 'byr':
            if  1920 <= int(output) <= 2002:
                possible = True
        if input == 'iyr':
            if 2010 <= int(output) <= 2020:
                possible = True
        if input == 'eyr':
            if 2020 <= int(output) <= 2030:
                possible = True
        if input == 'hgt':
            if output[-2:] in {'cm', 'in'}:
                if (output[-2:] == 'cm') and (150 <= int(output[:-2]) <= 193):
                    possible = True
                elif (output[-2:] == 'in') and (59 <= int(output[:-2]) <= 76):
                    possible = True
        if input == 'hcl':
            if re.search('^#(\d|[a-f]){6}$', output) is not None:
                possible = True
        if input == 'ecl':
            if output in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
                possible = True
        if input == 'pid':
            if re.search('^\d{9}$', output) is not None:
                possible = True
        if possible:
            fine += 1

    return fine == 7

print([check(z) for z in data].count(True))
