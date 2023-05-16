text = [int(x) for x in open('inputtxt/day10input.txt').read().splitlines()]
text.append(0)
text.sort()
text.append(max(text) + 3)

counter_one, counter_two = 0, 0
for x in range(len(text) - 1):
    distance = text[x + 1] - text[x]
    if distance == 1:
        counter_one += 1
    if distance == 3:
        counter_two += 1

print(counter_one * counter_two)

text_x = list(map(int, open('inputtxt/day10input.txt').read().splitlines()))
text_x.sort()
text_x = text_x + [max(text_x) + 3]
answer = {}
answer[0] = 1

for x in text_x:
    answer[x] = answer.get(x - 1, 0) + answer.get(x - 2, 0) + answer.get(x - 3, 0)

print(answer[text_x[-1]])


