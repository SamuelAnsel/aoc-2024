from collections import defaultdict


input_text = open("input.txt").read()

rules, updates = input_text.split("\n\n")
rules = rules.split("\n")
updates = updates.split("\n")

after = defaultdict(list)

for k, v in [rule.split("|") for rule in rules]:
    after[k] += [v]

middle = list()

for update in [x.split(',') for x in updates]:
    correct = True
    for i in range(1, len(update)):
        banned = set([item for j in range(i, len(update)) for item in after[update[j]]])

        if update[i - 1] in banned:
            correct = False
            break

    if correct:
        middle.append(int(update[len(update) // 2]))
    
print(sum(middle))