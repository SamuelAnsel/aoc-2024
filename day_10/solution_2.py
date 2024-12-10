import numpy as np


input_text = open("input.txt").read()

topo_map = np.array([[int(x) if x != '.' else -1 for x in row] for row in input_text.split("\n")])
M, N = topo_map.shape

directions = np.asarray([[0, 1], [0, -1], [1, 0], [-1, 0]])
tops = np.asarray(np.where(topo_map == 9)).reshape(2, -1).T

def downhill_walk(topo_map, start):
    walks = []
    stack = [(start, [start])]
    
    while stack:
        point, path = stack.pop()
        height = topo_map[point[0], point[1]]
        
        if height == 0:
            walks.append(path)
            continue
        
        for direction in directions:
            next_point = point + direction
            
            if next_point[0] < 0 or next_point[0] >= M or next_point[1] < 0 or next_point[1] >= N:
                continue
            
            if topo_map[next_point[0], next_point[1]] == height - 1:
                stack.append((next_point, path + [next_point]))
    
    return walks

coordinates = list()

for top in tops:
    walks = downhill_walk(topo_map, top)

    for walk in walks:
        coordinates += [f"{walk[0][0]}{walk[0][1]}{walk[-1][0]}{walk[-1][1]}"]

print(len(coordinates))