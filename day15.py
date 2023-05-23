text = [16, 1, 0, 18, 12, 14, 19]
from copy import deepcopy
text_x = deepcopy(text)
memory = {}

for index, number in enumerate(text):
    if index != len(text) - 1:
        memory[number] = index

while len(text_x) < 30000000:
    previous = text_x[-1]
    pprevious = memory.get(previous, -1)
    memory[previous] = len(text_x) - 1
    if pprevious == -1:
        upcoming = 0
    else:
        upcoming = len(text_x) - 1 - pprevious
    text_x.append(upcoming)
    if len(text_x) == 2020:
        print(upcoming)
print(text_x[-1])



