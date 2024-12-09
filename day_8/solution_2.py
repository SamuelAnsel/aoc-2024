import numpy as np


input_text = open("input.txt").read()

city_map = np.array([list(row) for row in input_text.split("\n")])
M, N = city_map.shape

frequencies = set(input_text)
frequencies.remove(".")
frequencies.remove("\n")

def city_block_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def is_node(point, antennas, freq):
    N = len(antennas[freq])

    for i in range(N):
        for j in range(i + 1, N):
            a1, a2 = antennas[freq][i], antennas[freq][j]
            alligned = (a1[1] - a2[1]) * (a1[0] - point[0]) == (a1[1] - point[1]) * (a1[0] - a2[0])

            if alligned:
                return True
        
    return False

antennas = {}

for freq in frequencies:
    antennas[freq] = np.asarray(np.where(city_map == freq)).reshape(2, -1).T

node_count = 0

for i in range(M):
    for j in range(N):
        for freq in frequencies:
            if is_node((i, j), antennas, freq):
                city_map[i, j] = "#"
                node_count += 1

                break

print(node_count)