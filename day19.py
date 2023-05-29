text = open('inputtxt/day19input.txt').read()
rule_text, messages = [line.splitlines() for line in text.split('\n\n')]

def run(string, rules):
    if string == '' or rules == []:
        return string == '' and rules == []
    rule = rules_list[rules[0]]
    if '"' in rule:
        if string[0] in rule:
            return run(string[1:], rules[1:])
        else:
            return False
    else:
        return any(run(string, r + rules[1:]) for r in rule)

def parse(string):
    first, second = string.split(': ')
    if '"' not in second:
        second = [[int(rule) for rule in line.split()] for line in second.split('|')]
    return (int(first), second)

rules_list = dict(parse(string) for string in rule_text)
print(sum(run(message, [0]) for message in messages))
rule_text += ['8: 42 | 42 8', '11: 42 31 | 42 11 31']
rules_list = dict(parse(string) for string in rule_text)
print(sum(run(message, [0]) for message in messages))