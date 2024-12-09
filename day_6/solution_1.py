import numpy as np
from collections import OrderedDict


input_text = open("input.txt").read()

patrol_map = np.array([list(row) for row in input_text.split("\n")])
M, N = patrol_map.shape

direction = OrderedDict({
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
})

valid_directions = list(direction.keys())

def update(patrol_map):
    new_patrol_map = np.copy(patrol_map)
    valid = True

    i, j = np.where(np.isin(patrol_map, valid_directions))
    i, j = i[0], j[0]

    current = new_patrol_map[i][j]
    move = direction[current]

    new_patrol_map[i][j] = "X"

    if i + move[0] < 0 or i + move[0] >= M or j + move[1] < 0 or j + move[1] >= N:
        valid = False
        return new_patrol_map, valid
    
    if new_patrol_map[i + move[0]][j + move[1]] == "#":
        current = valid_directions[(valid_directions.index(current) + 1) % 4]
        move = direction[current]

    new_patrol_map[i + move[0]][j + move[1]] = current

    return new_patrol_map, valid

valid = True

while valid:
    patrol_map, valid = update(patrol_map)

print(np.sum(patrol_map == 'X'))