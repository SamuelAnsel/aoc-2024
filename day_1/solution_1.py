input_text = open("input.txt").read()

L = [x.split('   ') for x in input_text.split('\n')]
A = sorted([int(x[0]) for x in L])
B = sorted([int(x[1]) for x in L])
distances = list()

for a, b in zip(A, B):
    distances += [abs(a - b)]
    
print(sum(distances))