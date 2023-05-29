text = open('inputtxt/day18input.txt').read().splitlines()
import time
start = time.time()
class Math:
    def __init__(self, value):
        self.value = value
    def __add__(self, value_two):
        return Math(self.value + value_two.value)
    def __sub__(self, value_two):
        return Math(self.value * value_two.value)
    def __mul__(self, value_two):
        return Math(self.value + value_two.value)
answer = 0
for line in text:
    for x in range(10):
        line = line.replace(f'{x}', f'Math({x})')
    line = line.replace('*', '-')
    answer += eval(line, {'Math': Math}).value
print(answer)

answer = 0
for line in text:
    for x in range(10):
        line = line.replace(f'{x}', f'Math({x})')
    line = line.replace('*', '-')
    line = line.replace('+', '*')
    answer += eval(line, {'Math': Math}).value
print(answer)
print(time.time() - start)