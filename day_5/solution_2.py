from collections import defaultdict
from functools import cmp_to_key


input_text = open("input.txt").read()
input_text = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

rules, updates = input_text.split("\n\n")
rules = rules.split("\n")
updates = updates.split("\n")

after = defaultdict(list)

for k, v in [rule.split("|") for rule in rules]:
    after[k] += [v]

middle = list()

def greater(a, b):
    print(a, b)
    print(a in after[b])
    return a in after[b]

for update in [x.split(',') for x in updates]:
    correct = True

    for i in range(1, len(update)):
        banned = set([item for j in range(i, len(update)) for item in after[update[j]]])

        if update[i - 1] in banned:
            correct = False
            update = sorted(update, key=cmp_to_key(greater))
            print(update)
            break


    if not correct:
        print(update)
        middle.append(int(update[len(update) // 2]))
    
print(sum(middle))