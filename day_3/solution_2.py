import re

input_text = open("input.txt").read()

products = list()
enabled = True

for match, a, b in re.findall(r"(don't\(\)|do\(\)|mul\((\d+),(\d+)\))", input_text):
    if match == "do()":
        enabled = True
    elif match == "don't()":
        enabled = False
    elif enabled:
        products.append(int(a) * int(b))

print(sum(products))