text = open('inputtxt/day1input.txt').read().splitlines()

for x in range(len(text)):
    for y in range(x, len(text)):
        if int(text[x]) + int(text[y]):
            print(int(text[x]) * int(text[y]))
        for z in range(y, len(text)):
            if int(text[x]) + int(text[y]) + int(text[z]) == 2020:
                print(int(text[x]) * int(text[y]) * int(text[z]))
