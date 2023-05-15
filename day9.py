text = open('inputtxt/day9input.txt').read().splitlines()


def possible(numbers, total):
    for x in range(len(numbers)):
        for y in range(x + 1, len(numbers)):
            if int(numbers[x]) + int(numbers[y]) == int(total):
                return True
    return False

counter = 0
answer = 0
for x in range(25, len(text)):
    if not possible(text[counter:x], text[x]):
        print(text[x])
        answer = text[x]
        break
    counter += 1

for x in range(len(text)):
    for y in range(x + 2, len(text)):
        if sum(int(z) for z in text[x:y]) == int(answer):
            print(min(int(z) for z in text[x:y]) + max(int(z) for z in text[x:y]))
            break

