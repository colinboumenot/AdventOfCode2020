text = open('inputtxt/day5input.txt').read().splitlines()

for x in range(len(text)):
    text[x] = text[x].replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0')

text.sort()
print(int(text[-1], 2))

for x in range(1, len(text)):
    if int(text[x],2) - int(text[x-1],2) != 1:
        print(int(text[x],2) - 1)
        break