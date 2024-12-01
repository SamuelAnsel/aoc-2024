from collections import Counter

input_text = open("input.txt").read()

L = [x.split('   ') for x in input_text.split('\n')]
A = [int(x[0]) for x in L]
count = Counter([int(x[1]) for x in L])
similarity = list()

for a in A:
    similarity += [a * count.get(a, 0)]
    
print(sum(similarity))