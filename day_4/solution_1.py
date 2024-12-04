import numpy as np

input_text = open("input.txt").read()

matrix = np.array([[c for c in row] for row in input_text.split("\n")])
word = "XMAS"
rev = word[::-1]

count = 0

diagonals = ["".join(matrix.diagonal(i)) for i in range(-matrix.shape[0] + 1, matrix.shape[1])]
diagonals += ["".join(matrix[::-1, :].diagonal(i)) for i in range(-matrix.shape[0] + 1, matrix.shape[1])]
rows = ["".join(row) for row in matrix]
cols = ["".join(col) for col in matrix.T]

text = " ".join(diagonals + rows + cols)
count += text.count(word) + text.count(rev)

print(count)