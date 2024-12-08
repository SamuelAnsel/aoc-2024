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

def update(patrol_map):
    new_patrol_map = np.copy(patrol_map)
    valid = True
    found = False

    for i in range(0, M):
        for j in range(0, N):
            current = new_patrol_map[i][j]

            if current in direction:
                found = True
                new_patrol_map[i][j] = "X"
                move = direction[current]

                if i + move[0] < 0 or i + move[0] >= M or j + move[1] < 0 or j + move[1] >= N:
                    valid = False
                    break
                
                if new_patrol_map[i + move[0]][j + move[1]] == "#":
                    L = list(direction.keys())
                    current = L[(L.index(current) + 1) % 4]
                    move = direction[current]

                new_patrol_map[i + move[0]][j + move[1]] = current
                break
        
        if found:
            break
    
    return new_patrol_map, valid

valid = True

while valid:
    patrol_map, valid = update(patrol_map)

print(np.sum(patrol_map == 'X'))