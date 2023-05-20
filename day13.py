text = open('inputtxt/day13input.txt').read().splitlines()
departure = int(text[0])
busses = set(text[1].split(','))
busses.remove('x')

bus = 0
gap = 999999999
for x in busses:
    if int(x) - (departure % int(x)) < gap:
        bus = int(x)
        gap = int(x) - (departure % int(x))

print(gap * bus)

busses = [(index, int(id)) for index, id in enumerate(text[1].split(',')) if id != 'x']
time = 0
jump = busses[0][1]
for index, id in busses[1:]:
    while (time + index) % id != 0:
        time += jump
    jump *= id
print(time)