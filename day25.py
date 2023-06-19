text = open('inputtxt/day25input.txt').read().splitlines()
modder = 20201227

product = 1
for x in range(1000000000000000000000000):
    if product == int(text[0]):
        break
    product = (product * 7) % modder

print(pow(int(text[1]), x, modder))