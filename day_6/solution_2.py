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

def next_direction(current):
    return valid_directions[(valid_directions.index(current) + 1) % 4]

def update(patrol_map):
    new_patrol_map = np.copy(patrol_map)
    valid = True
    has_loop = False

    i, j = np.where(np.isin(patrol_map, valid_directions))
    i, j = i[0], j[0]

    current = new_patrol_map[i][j]
    move = direction[current]

    if i + move[0] < 0 or i + move[0] >= M or j + move[1] < 0 or j + move[1] >= N:
        valid = False
        return new_patrol_map, valid, has_loop
    
    next_dir = next_direction(current)

    if new_patrol_map[i + move[0]][j + move[1]] == "#":
        current = next_dir
        move = direction[current]
    else:
        dir = next_dir # prevoir demi tour

        if dir in ["^", "v"]:
            wall = np.where(new_patrol_map[:, j] == "#")[0]

            if wall.shape[0] > 0:
                wall = wall[0]

                after = direction[dir][0] * (wall - i) > 0

                if after and new_patrol_map[wall - direction[dir][0], j] == "X":
                    has_loop = True

        elif dir in [">", "<"]:
            wall = np.where(new_patrol_map[i, :] == "#")[0]

            if wall.shape[0] > 0:
                wall = wall[0]

                after = direction[dir][1] * (wall - j) > 0

                if after and new_patrol_map[i , wall - direction[dir][1]] == "X":
                    has_loop = True

    new_patrol_map[i][j] = "X"
    new_patrol_map[i + move[0]][j + move[1]] = current

    return new_patrol_map, valid, has_loop

valid = True
count = 0

while valid:
    patrol_map, valid, has_loop = update(patrol_map)

    if has_loop:
        count += 1

print(count)