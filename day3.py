text = open('inputtxt/day3input.txt').read().splitlines()

def search(x, y):
    count = 0
    row = 0
    col = 0
    for _ in range(len(text)):
        if row >= len(text):
            break
        if text[row][col] == '#':
            count += 1
        row += y
        col = (col + x) % len(text[0])
    return count

print(search(3, 1))
answer = 1
print(search(1,2))

answer *= ((search(1,1) * search(3, 1) * search(5,1)) * search(7,1) * search(1,2))
print(answer)


