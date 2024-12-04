import re

input_text = open("input.txt").read()

products = list()

for i in re.findall(r"mul\((\d+),(\d+)\)", input_text):
    products.append(int(i[0]) * int(i[1]))

print(sum(products))